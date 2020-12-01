import numpy as np
import requests
import matplotlib.pyplot as plt
from matplotlib.dates import datetime as dt
import time


time.ctime

fig, ax = plt.subplots()

by_price = 19530


def test():
	headers = {'Content-Type': 'application/x-www-form-urlencoded'}
	data = {'pair':'BTC_USD'}
	
	r = requests.post('https://api.exmo.com/v1.1/trades', headers = headers, data = data)
	

	now_price = float(r.json()['BTC_USD'][0]['price'])
	now_date = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(r.json()['BTC_USD'][0]['date']+10800))
	date = []
	price = []

	for i in r.json()['BTC_USD']:
		price.append(float(i['price']))
		date.append(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(i['date']+10800)))

	#print(date)
	return price,date,now_price,now_date


price,date_s,now_price,now_date_in = test()

date = [dt.datetime.strptime(d, '%Y-%m-%d %H:%M:%S') for d in date_s]

now_date = dt.datetime.strptime(now_date_in, '%Y-%m-%d %H:%M:%S')


#y1 = 19200
#x1 = 5

ax.plot(date,price)
ax.scatter(now_date,now_price)
ax.hlines(now_price*0.99, date[0],date[-1] )
ax.hlines(now_price*1.01, date[0],date[-1] )

#ax.text(x1, y1+10, 'By',fontsize = 20)

ax.set(title = 'test')



if __name__ == '__main__':

	plt.show()
	#test()
