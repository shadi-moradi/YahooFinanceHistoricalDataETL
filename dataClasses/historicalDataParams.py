from dataclasses import dataclass
from datetime import datetime
from enum import Enum

class Intervals(Enum):
    Daily = "1d"
    Weekly = "7d"
    Monthly = "30d"

class Ranges(Enum):
    YTD = 1 # the period of time beginning the first day of the current year 
    oneYear = 2

@dataclass
class HistoricalDataParams:
    symbol: str
    startDate: datetime = None
    endDate: datetime = None
    range: Ranges = None
    interval: Intervals = Intervals.Daily
