from addict import Dict

def getPostgresConnectionConfig():
    return {
        'host': 'localhost',
        'user': 'postgres',
        'password': 'welcome',
        'database': 'stock',
        'port': '5432',
    }

yahooFinanceJSONAPI = 'https://query1.finance.yahoo.com/v8/finance/chart'
yahooFinanceCSVAPI = 'https://query1.finance.yahoo.com/v7/finance/download'

historicalDataFields = Dict(
    {
        'date': 'date',
        'open': 'open',
        'close': 'close',
        'high': 'high',
        'low': 'low',
        'adjclose': 'adjclose',
        'symbol': 'symbol',
        'volume': 'volume',
        'intervalsymboldate': 'intervalsymboldate',
        'interval': 'interval',
    }
)
