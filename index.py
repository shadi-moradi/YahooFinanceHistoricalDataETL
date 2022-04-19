from datetime import datetime
import config
from historicalDataService import historicalDataService, EndPointType
import historicalDataRepository
import plot
from dataClasses.historicalDataParams import HistoricalDataParams, Intervals, Ranges

try:
    params = HistoricalDataParams(
        symbol = 'BTC-USD',
        range = Ranges.YTD, # range takes precedence over startDate and endDate
        startDate = None, # sample data: datetime(2021, 11, 19),
        endDate = None, # sample data: datetime(2022, 1, 17),
        interval = Intervals.Daily,
    )

    result = historicalDataRepository.createTable()
    print(result.description)

    historicalDataService.YahooFinance_ETL(EndPointType.JSON, params)
    # historicalDataService.YahooFinance_ETL(EndPointType.CSV, params)

    myPlot = plot.plotHistoricalData()
    myPlot.plot(
        params= params,
        kind= plot.PlotKind.candleStick,
        title= 'Daily BTC-USD Price',
        xLabel= 'Date',
        yLabel= 'Quotes',
    )
    myPlot.plot(
        params= params,
        kind= plot.PlotKind.line,
        title= 'Daily BTC-USD Close Price',
        xLabel= 'Date',
        yLabel= 'Close Price',
        xField= config.historicalDataFields.date,
        yField= config.historicalDataFields.close
    )

except Exception as err:
    print(err)



