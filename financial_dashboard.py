#Bruce Reyes 
#INST126 
#This is a financial dashboard that a user can use. I will be using the yfinance API, numpy and bokeh for visualization
#I was able to attain information about how to use it on their websites

#import all factors needed to run this program
#rename some imports that will called back in your code to something shorter
import math
import datetime as dt
import numpy as np
import yfinance as yf

#import all of things needed to visualize the dashboard
from bokeh.io import curdoc
from bokeh.plotting import figure 
from bokeh.layouts import row, column
from bokeh.models import TextInput, Button, DatePicker, MultiChoice

#function that will allow you to compare two financial dashboards at the same time using tickers
def LoadData(ticker1, ticker2, start, end):
    DataFrame1: yf.download(ticker1, start, end)
    DataFrame2: yf.download(ticker1, start, end)
    return DataFrame1, DataFrame2

#function that will actually graph the data visually
def GraphData(data, indicators, sync_axis=None):
    pass

#function for what will happen to button when clicked
def OnButtonClick(ticker1, ticker2, start, end, indicators):
    pass

Stock1Text = TextInput(title = "Stock 1")
Stock2Text = TextInput(title = "Stock 2")

#allows user to have a range of dates to choose from going from whenever the user is using a code to 2000
DatePickFrom = DatePicker(title= "Start Date", value = "2020/01/01",
                            MinDate = "2000/01/01", max_date = dt.datetime.now().strftime("%Y/%M/%D"))
                            







