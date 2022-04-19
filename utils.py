import datetime
from dataClasses.historicalDataParams import Intervals, Ranges
from plot import PlotKind

def convertTimestampToDate(timestamp):
    return datetime.date.fromtimestamp(timestamp)

def convertTimestampsToDates(timestamps):
    result = []
    for timestamp in timestamps:
        result.append(convertTimestampToDate(timestamp))
    return result

def convertDateToTimestamp(date):
    return int(date.timestamp())

def isValidDate(date):
    return type(date) is datetime.datetime

def isValidRange(range):
    return type(range) is Ranges

def isValidInterval(interval):
    return (interval != None) and (type(interval) is Intervals)

def isValidSymbol(symbol):
    return (symbol != None) and symbol == "BTC-USD"

def isValidPlotKind(kind):
    return (kind != None) and type(kind) is PlotKind

def rangeToDate(range):
    today = datetime.datetime.today()
    endDate = today
    startDate = None

    if range == Ranges.YTD:
        startDate = today.replace(day=1, month=1)
    elif range == Ranges.oneYear:
        days = datetime.timedelta(365)
        startDate = endDate - days
    return startDate, endDate




