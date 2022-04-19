import mplfinance as mpl
import matplotlib.pyplot as plt
from customExceptions.InvalidParameterException import InvalidParameterException
import historicalDataService
import utils
from enum import Enum
import config

class PlotKind(Enum):
    line = "line"
    candleStick = "candleStick"

class plotHistoricalData:
    def plot(self, params, kind, title, xLabel, yLabel, xField=None, yField=None): # set default value for xField and yField to None, because for Candlestick there is no need to set them
        if not utils.isValidPlotKind(kind):
            raise InvalidParameterException("plot kind must be set to one of pre-defined values")

        df = historicalDataService.historicalDataService.getData(params)

        if (kind == PlotKind.candleStick):
            self.__plotCandlestick(df, title, xLabel, yLabel)
        else:
            self.__plotOtherTypes(df, kind, title, xLabel, yLabel, xField, yField)

    def __plotCandlestick(self, dataFrame, title, xLabel, yLabel):
        dataFrame = dataFrame.set_index(config.historicalDataFields.date)
        mpl.plot(
            dataFrame,
            type = 'candle',
            # style = 'yahoo',
            title = title,
            ylabel = yLabel,
        )

    def __plotOtherTypes(self, dataFrame, kind, title, xLabel, yLabel, xField, yField):
        dataFrame.plot(x=xField, y=yField, kind=kind.value)
        plt.title(title)
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.show()