import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

stockdata = pd.read_csv('neogrid.csv', infer_datetime_format = False, parse_dates = ['Date'], index_col='Date')
plt.plot(stockdata['Close'])