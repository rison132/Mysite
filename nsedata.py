import pandas as pd
import csv
from nsepy import get_history
import pandas_datareader.data as web
from datetime import date
import pickle
import os


# data = get_history(symbol="SBIN", start=date(2015,1,1), end=date(2015,1,31))
# print(data.head())

def save_nse500_tickers():
	data = pd.read_csv("NSE500tickers.csv")
	tickers=[]
	# data.set_index('Symbol',inplace=True)
	# s = pd.DataFrame( data, columns=['Symbol'])

	# print(s)
	
	for key, value in data.items():
		tickers.append(value)


	with open("Newnse500tickers.pickle","wb") as f:
		pickle.dump(tickers,f)

	
	return tickers
save_nse500_tickers()

def get_data_from_nse(reload_sp500=False):
	
	if reload_sp500:
		tickers=save_nse500_tickers()
	else:
		with open("Newnse500tickers.pickle","rb") as f:
			tickers=pickle.load(f)

	if not os.path.exists('stock_nse'):
		os.makedirs('stock_nse')

		# start =date.datetime(2000,1,1)
		# end=date.datetime.now()

	for ticker in tickers:
		print(ticker)
		if not os.path.exists('stock_nse/{}.csv'.format(ticker)):
			df =get_history(symbol=ticker,
                    start=date(2015,1,1), 
                    end=date(2019,2,13))
			
			# df = web.DataReader(ticker, 'yahoo', start, end)
			df.to_csv('stock_nse/{}.csv'.format(ticker))
		else:
			print("Already Have {}".format(ticker))
get_data_from_nse()


# with open("Newnse500tickers.pickle","rb") as f:
# 			tickers=pickle.load(f)
# print(tickers)