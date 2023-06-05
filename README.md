<!DOCTYPE html>
<html>
<body>
  <h1>Bazaar - Where the Stock Buzz</h1>

  <p>This project is a web application that predicts stock prices using LSTM model. It allows users to enter a stock symbol, select a date range, and view the actual and predicted prices.</p>

  <h2>Table of Contents</h2>
  <ul>
    <li><a href="#demo">Demo</a></li>
    <li><a href="#features">Features</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#contributing">Contributing</a></li>
  </ul>

  <h2 id="demo">Demo</h2>

<p>You can find a live demo of the application after you download and run the code<a href="http://localhost:8501/">here</a>.</p>
  
  <h2 id="features">Features</h2>
  <ul>
    <li>Enter a stock symbol and select a date range.</li>
    <li>View the historical stock data for the selected stock.</li>
    <li>Calculate the rolling mean and standard deviation of the closing prices.</li>
    <li>Train a LSTM model using the rolling mean and standard deviation as features.</li>
    <li>Predict the future stock prices for a specified time period.</li>
    <li>Visualize the actual and predicted prices on a line chart.</li>
  </ul>

  <h2 id="getting-started">Getting Started</h2>

  <h3>Prerequisites</h3>
  <ul>
    <li>Python 3.7 or higher</li>
    <li>pip package manager</li>
  </ul>

  <h3>Installation</h3>
  <ol>
    <li>Clone the repository:</li>
    <code>git clone &lt;https://github.com/Jainil-coder/Bazaar-Stock-Price-Prediction&gt;</code>
    <li>Install the required dependencies:</li>
    <code>pip install -r requirements.txt</code>
  </ol>

  <h2 id="usage">Usage</h2>
  <ol>
    <li>Run the application:</li>
    <code>streamlit run Bazaar.py</code>
    <li>Open the application in your web browser:</li>
    <code>
      Local URL: http://localhost:8501<br>
      Network URL: http://&lt;your-ip-address&gt;:8501
    </code>
    <li>Enter a stock symbol and select a date range.</li>
    <li>View the historical stock data and the visualized prediction.</li>
  </ol>

  <h2 id="built-with">Built With</h2>
  <ul>
    <li><a href="https://streamlit.io/">Streamlit</a> - The web framework used for building the user interface.</li>
    <li><a href="https://github.com/ranaroussi/yfinance">yfinance</a> - Used to retrieve stock data from Yahoo Finance.</li>
    <li><a href="[https://scikit-learn.org/](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html)">MinMaxScaler</a> - Used to process data.</li>
    <li><a href="https://pandas.pydata.org/">Pandas</a> - Used for data manipulation and analysis.</li>
    <li><a href="https://plotly.com/">Plotly</a> - Used for interactive data visualization.</li>
    <li><a href="https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM">LSTM</a> - Used to train the LSTM model.</li>
  </ul>

  <h2 id="contributing">Contributing</h2>
  <p>Contributions are welcome! Please fork the repository and submit a pull request.</p>

</body>
</html>
