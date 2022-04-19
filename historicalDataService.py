import pandas as pd
from YF_HistoricalDataManipulators.YF_HistoricalDataManipulator import YF_HistoricalDataManipulator
from YF_HistoricalDataManipulators.YF_HistoricalDataManipulatorFromCSV import YF_HistoricalDataManipulatorFromCSVEndPoint
from YF_HistoricalDataManipulators.YF_HistoricalDataManipulatorFromJSON import YF_HistoricalDataManipulatorFromJSONEndPoint
import historicalDataRepository
from enum import Enum

class EndPointType(Enum):
    JSON = 1
    CSV = 2

class historicalDataService:
    def YahooFinance_ETL(EndPointType, params):
        resultInDataFrame = None

        if EndPointType == EndPointType.JSON:
            YF_JSONEndPoint = YF_HistoricalDataManipulatorFromJSONEndPoint()
            resultInDataFrame = YF_JSONEndPoint.ET(params)
        elif EndPointType == EndPointType.CSV:
            YF_CSVEndPoint = YF_HistoricalDataManipulatorFromCSVEndPoint()
            resultInDataFrame = YF_CSVEndPoint.ET(params)

        result = historicalDataService.__loadHistoricalDataFrame(resultInDataFrame)
        print(result.description)

    def __loadHistoricalDataFrame(data):  # insert data into database
        if (len(data) > 0):
            status = historicalDataRepository.loadDataFrame(data)
            return status

    def getData(params):
        validParams = YF_HistoricalDataManipulator.validateAndSetParameters(params)
        result = historicalDataRepository.getData(validParams.interval, validParams.symbol, validParams.startDate, validParams.endDate)
        resultInDataFrame = pd.DataFrame(result.data)
        resultInDataFrame.date = pd.to_datetime(resultInDataFrame.date)
        resultInDataFrame.open = pd.to_numeric(resultInDataFrame.open)
        resultInDataFrame.high = pd.to_numeric(resultInDataFrame.high)
        resultInDataFrame.low = pd.to_numeric(resultInDataFrame.low)
        resultInDataFrame.close = pd.to_numeric(resultInDataFrame.close)
        return resultInDataFrame




