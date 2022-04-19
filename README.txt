you have to install these modules:
 - psycopg2
 - pandas
 - addict
 - mplfinance
 - matplotlib

steps:
 - create a database called 'stock'
 - set your database details in 'config.py'
 - index.py is the main script
 - run 'historicalDataRepository.createTable()' method to create required table
 - if you need change parameters' value at the start of the index.py file
 - call 'historicalDataService.YahooFinance_ETL' function with your prefered endpoint type EndPointType.JSON or EndPointType.CSV.
 - call plot to show historical data

python version: 3.10.2

Description:
you can add historical data based on different intervals, dates and symbols