import streamlit as st
import yfinance as yf
from datetime import date, timedelta, datetime
import pandas as pd
import numpy as np
import plotly.graph_objs as go
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

st.title("Bazaar - Where the stock buzz")

symbol = st.sidebar.text_input("Enter stock symbol (e.g., AAPL for Apple):", "RELIANCE.NS")
START = "2015-01-01"

start_date = st.sidebar.date_input("Start date:", pd.to_datetime(START))
end_date = st.sidebar.date_input("End date:", pd.to_datetime(date.today().strftime("%Y-%m-%d")))

stock_data = yf.download(symbol, start=start_date, end=end_date)

if stock_data.empty:
    st.error("No data found for the selected stock symbol and date range.")
else:
    # Display the stock data
    st.subheader(symbol + " - Stock Data")
    st.write(stock_data)

def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Open'], name="Open price"))
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'], name="Close price"))
    fig.update_layout(title_text='Stock Price Visualization', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

plot_raw_data()

# Prepare the data for LSTM
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(stock_data['Close'].values.reshape(-1, 1))

# Define the training data
train_data = scaled_data[:int(0.8 * len(scaled_data))]
x_train, y_train = [], []
for i in range(20, len(train_data)):
    x_train.append(train_data[i-20:i, 0])
    y_train.append(train_data[i, 0])
x_train, y_train = np.array(x_train), np.array(y_train)
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

# Build the LSTM model
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(LSTM(units=50))
model.add(Dense(1))

# Compile and train the model
model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(x_train, y_train, epochs=25, batch_size=32)

# Predict future prices
test_data = scaled_data[int(0.8 * len(scaled_data)) - 20:]
x_test = []
for i in range(20, len(test_data)):
    x_test.append(test_data[i-20:i, 0])
x_test = np.array(x_test)
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
predicted_prices = model.predict(x_test)
predicted_prices = scaler.inverse_transform(predicted_prices)

# Create a dataframe for the future predicted price
future_dates = pd.date_range(start=end_date, periods=len(predicted_prices))
future_data = pd.DataFrame(index=future_dates, data={"Predicted Price": predicted_prices.flatten()})

# Combine actual and predicted data
combined_data = pd.concat([stock_data["Close"], future_data["Predicted Price"]])

fig = go.Figure()
fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data["Close"], name="Actual Price"))
fig.add_trace(go.Scatter(x=future_data.index, y=future_data["Predicted Price"], name="Predicted Price"))
fig.update_layout(title_text="Stock Price Prediction", xaxis_title="Date", yaxis_title="Price", xaxis_rangeslider_visible=True)
st.plotly_chart(fig)
