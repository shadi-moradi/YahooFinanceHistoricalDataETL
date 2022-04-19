import connectionManager

def createTable():
    command = """
        CREATE TABLE IF NOT EXISTS historicalData (
            id SERIAL PRIMARY KEY,
            interval VARCHAR(50) NOT NULL,
            symbol VARCHAR(50) NOT NULL,
            date DATE NOT NULL,
            intervalsymboldate TEXT UNIQUE NOT NULL, --added to make sure by running multiple times duplicated data would not be inserted
            open DECIMAL NOT NULL,
            high DECIMAL NOT NULL,
            low DECIMAL NOT NULL,
            close DECIMAL NOT NULL,
            adjclose DECIMAL NOT NULL, --Adjusted Close is the closing price after adjustments for all applicable splits and dividend distributions
            volume BIGINT NOT NULL
        )
        """
    result = connectionManager.execute(command)
    return result

def loadDataFrame(df):
    command = """
        INSERT INTO historicalData (interval, symbol, date, intervalsymboldate, open, high, low, close, adjclose, volume) 
        VALUES (%(interval)s, %(symbol)s, %(date)s, %(intervalsymboldate)s, %(open)s, %(high)s, %(low)s,%(close)s,%(adjclose)s,%(volume)s)
    """
    result = connectionManager.executeMany(command, df)
    return result


def getData(interval, symbol, startDate, endDate):
    command = """
        SELECT *
        FROM historicalData
        WHERE date >= %(startDate)s and date <= %(endDate)s and symbol = %(symbol)s and interval = %(interval)s
    """
    params = {
        "symbol": symbol,
        "startDate" : startDate,
        "endDate": endDate,
        "interval": interval,
    }

    result = connectionManager.selectData(command, params)
    return result