# Script to extract the historical prices of the S&P 500

# Author: Matthew Myers

# Import packages
import yfinance as yf
import pandas as pd

# Start date and end dates of dataset
start_date = '2019-09-16'
end_date = '2023-12-02'

# Get the S&P 500 data
sp500_data = yf.download('^GSPC', start=start_date, end=end_date)

# Print the S&P 500 data
print(sp500_data)

# Define function to extract S&P 500 data

# Return extracted data as a dataframe

# Define function to return dataframe when script is called
