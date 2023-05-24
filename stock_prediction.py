# import streamlit as st
# import yfinance as yf
# from datetime import date, timedelta
# from sklearn.linear_model import LinearRegression
# import pandas as pd
# import plotly.graph_objs as go
# import matplotlib.pyplot as plt

# st.title("Stock Price Prediction")

# symbol = st.sidebar.text_input("Enter stock symbol (e.g., AAPL for Apple):", "AAPL")
# START = "2015-01-01"

# start_date = st.sidebar.date_input("Start date:", pd.to_datetime(START))
# end_date = st.sidebar.date_input("End date:", pd.to_datetime(date.today().strftime("%Y-%m-%d")))

# stock_data = yf.download(symbol, start=start_date, end=end_date)

# if stock_data.empty:
#     st.error("No data found for the selected stock symbol and date range.")
# else:
#     # Display the stock data
#     st.subheader("Stock Data")
#     st.write(stock_data)

# def plot_raw_data():
#     fig = go.Figure()
#     fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Open'], name="stock_open"))
#     fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'], name="stock_close"))
#     fig.update_layout(title_text='Stock Price', xaxis_rangeslider_visible=True)
#     st.plotly_chart(fig)

# plot_raw_data()

# # Calculate the rolling mean and standard deviation
# stock_data["RollingMean"] = stock_data["Close"].rolling(window=20).mean()
# stock_data["RollingStd"] = stock_data["Close"].rolling(window=20).std()

# # Create a new dataframe with the selected features
# df_features = stock_data[["Close", "RollingMean", "RollingStd"]].copy()

# # Drop rows with missing values
# df_features.dropna(inplace=True)

# if len(df_features) > 20:  # Check if there are sufficient data points for prediction
#     # Split the dataset into features and target variable
#     X = df_features[["RollingMean", "RollingStd"]]
#     y = df_features["Close"]

#     # Train the linear regression model
#     model = LinearRegression()
#     model.fit(X, y)

#     # Predict future prices
#     period = 365  # Predict for 365 days ie. 1 year ahead
#     future_date = df_features.index[-1] + timedelta(days=1)
#     future_features = pd.DataFrame(index=[future_date])
#     future_features["RollingMean"] = df_features["RollingMean"].iloc[-1]
#     future_features["RollingStd"] = df_features["RollingStd"].iloc[-1]

#     future_price = model.predict(future_features.values.reshape(1, -1))

#     # Create a dataframe for the future predicted prices
#     future_data = pd.DataFrame(index=[future_date], data={"Predicted Price": future_price})

#     # Combine actual and predicted data
#     combined_data = pd.concat([df_features["Close"], future_data["Predicted Price"]])

#     fig = go.Figure()
#     fig.add_trace(go.Scatter(x=df_features.index, y=df_features["Close"], name="Actual Price"))
#     fig.add_trace(go.Scatter(x=future_data.index, y=future_data["Predicted Price"], name="Predicted Price"))
#     fig.update_layout(title_text="Stock Price Prediction", xaxis_title="Date", yaxis_title="Price", xaxis_rangeslider_visible=True)
#     st.plotly_chart(fig)
# else:
#     st.error("Insufficient data to predict future prices.")

import streamlit as st
import yfinance as yf
from datetime import date, timedelta, datetime
from sklearn.linear_model import LinearRegression
import pandas as pd
import plotly.graph_objs as go

st.title("Stock Price Prediction")

symbol = st.sidebar.text_input("Enter stock symbol (e.g., AAPL for Apple):", "AAPL")
START = "2015-01-01"

start_date = st.sidebar.date_input("Start date:", pd.to_datetime(START))
end_date = st.sidebar.date_input("End date:", pd.to_datetime(date.today().strftime("%Y-%m-%d")))

stock_data = yf.download(symbol, start=start_date, end=end_date)

if stock_data.empty:
    st.error("No data found for the selected stock symbol and date range.")
else:
    # Display the stock data
    st.subheader("Stock Data")
    st.write(stock_data)

def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Open'], name="stock_open"))
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'], name="stock_close"))
    fig.update_layout(title_text='Stock Price', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

plot_raw_data()

# Calculate the rolling mean and standard deviation
stock_data["RollingMean"] = stock_data["Close"].rolling(window=20).mean()
stock_data["RollingStd"] = stock_data["Close"].rolling(window=20).std()

# Create a new dataframe with the selected features
df_features = stock_data[["Close", "RollingMean", "RollingStd"]].copy()

# Drop rows with missing values
df_features.dropna(inplace=True)

if len(df_features) > 20:  # Check if there are sufficient data points for prediction
    # Split the dataset into features and target variable
    X = df_features[["RollingMean", "RollingStd"]]
    y = df_features["Close"]

    # Train the linear regression model
    model = LinearRegression()
    model.fit(X, y)

    # Predict future prices for 1 day ahead
    future_date = datetime.today() + timedelta(days=1)
    future_features = pd.DataFrame(index=[future_date])
    future_features["RollingMean"] = stock_data["RollingMean"].iloc[-1]
    future_features["RollingStd"] = stock_data["RollingStd"].iloc[-1]

    future_price = model.predict(future_features.values.reshape(1, -1))

    # Create a dataframe for the future predicted price
    future_data = pd.DataFrame(index=[future_date], data={"Predicted Price": future_price})

    # Combine actual and predicted data
    combined_data = pd.concat([df_features["Close"], future_data["Predicted Price"]])

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_features.index, y=df_features["Close"], name="Actual Price"))
    fig.add_trace(go.Scatter(x=future_data.index, y=future_data["Predicted Price"], name="Predicted Price"))
    fig.update_layout(title_text="Stock Price Prediction", xaxis_title="Date", yaxis_title="Price", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)
else:
    st.error("Insufficient data to predict future prices.")
