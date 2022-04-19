from YF_HistoricalDataManipulators.YF_HistoricalDataManipulator import YF_HistoricalDataManipulator
import config
import utils
import requests
import pandas as pd
from addict import Dict

class YF_HistoricalDataManipulatorFromJSONEndPoint(YF_HistoricalDataManipulator):
    def fetchDataFromEndPoint(self, params):
        queryStr = {
            "period1" : utils.convertDateToTimestamp(params.startDate),
            "period2" : utils.convertDateToTimestamp(params.endDate),
            "interval" : params.interval
        }
        url = f"{config.yahooFinanceJSONAPI}/{params.symbol}"
        res = requests.get(url, params=queryStr, headers={'User-agent': 'Chrome/91.0.4472.124'})
        return res

    def transformFetchedDataToDataFrame(self, fetchedData, fetchParams):
        content = Dict(fetchedData.json()).chart.result[0]
        prices = content.indicators.quote[0]
        adjclose = content.indicators.adjclose[0]
        timestamps = content.timestamp
        dates = utils.convertTimestampsToDates(timestamps)
        prices.update(adjclose)

        df = pd.DataFrame(prices)
        df[config.historicalDataFields.date] = dates
        df[config.historicalDataFields.symbol] = fetchParams.symbol
        df[config.historicalDataFields.interval] = fetchParams.interval
        df[config.historicalDataFields.intervalsymboldate] = df.interval + df.symbol + df.date.map(str)
        return df