
from YF_HistoricalDataManipulators.YF_HistoricalDataManipulator import YF_HistoricalDataManipulator
import config
import utils
import requests
import pandas as pd
import io

class YF_HistoricalDataManipulatorFromCSVEndPoint(YF_HistoricalDataManipulator):
    def fetchDataFromEndPoint(self, params):
        queryStr = {
            "period1" : utils.convertDateToTimestamp(params.startDate),
            "period2" : utils.convertDateToTimestamp(params.endDate),
            "interval" : params.interval
        }
        url = f"{config.yahooFinanceCSVAPI}/{params.symbol}"
        res = requests.get(url, params=queryStr, headers={'User-agent': 'Chrome/91.0.4472.124'}) # without passing the User-Agent in header it returns forbidden 403
        return res

    def transformFetchedDataToDataFrame(self, fetchedData, fetchParams):
        df = pd.read_csv(io.StringIO(fetchedData.content.decode('utf-8')), parse_dates=['Date'], skip_blank_lines=True)
        columnMap = {
            'Date' : config.historicalDataFields.date,
            'Open' : config.historicalDataFields.open,
            'High' : config.historicalDataFields.high,
            'Low' : config.historicalDataFields.low,
            'Close' : config.historicalDataFields.close,
            'Adj Close' : config.historicalDataFields.adjclose,
            'Volume' : config.historicalDataFields.volume,
        }
        df.rename(columns=columnMap, inplace=True)
        df[config.historicalDataFields.symbol] = fetchParams.symbol
        df[config.historicalDataFields.interval] = fetchParams.interval
        df[config.historicalDataFields.intervalsymboldate] = df.interval + df.symbol + df.date.map(lambda date: str(date.date()))
        return df
