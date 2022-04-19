from customExceptions.InvalidParameterException import InvalidParameterException
from dataClasses.historicalDataParams import HistoricalDataParams
import utils


class YF_HistoricalDataManipulator:
    def ET(self, params):
        try:
            validParams = self.validateAndSetParameters(params)
            data = self.fetchDataFromEndPoint(validParams)
            df = self.transformFetchedDataToDataFrame(data, validParams)
            return df

        except Exception as err:
            print(err)

    @staticmethod
    def validateAndSetParameters(historicalDataParams):
        startDate = None
        endDate = None

        if not utils.isValidSymbol(historicalDataParams.symbol):
            raise InvalidParameterException("symbol must be set to BTC-USD")

        if not utils.isValidInterval(historicalDataParams.interval):
            raise InvalidParameterException("interval must be set to one of pre-defined values")

        if historicalDataParams.range != None:
            if not utils.isValidRange(historicalDataParams.range):
                raise InvalidParameterException("range must be set to one of pre-defined values")
            else:
                startDate, endDate = utils.rangeToDate(historicalDataParams.range)
        else:
            if (historicalDataParams.startDate is None) or (not utils.isValidDate(historicalDataParams.startDate)):
                raise InvalidParameterException("startDate must be set and should be a valid datetime")

            if (historicalDataParams.endDate is None) or (not utils.isValidDate(historicalDataParams.endDate)):
                raise InvalidParameterException("endDate must be set and should be a valid datetime")

            startDate = historicalDataParams.startDate
            endDate = historicalDataParams.endDate

        finalParams = HistoricalDataParams(
            symbol = historicalDataParams.symbol,
            startDate = startDate,
            endDate = endDate,
            interval = historicalDataParams.interval.value
        )
        return finalParams