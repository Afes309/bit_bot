import requests
from time import sleep


headers = {'Content-Type': 'application/x-www-form-urlencoded'}
data = {'pair':'BTC_USD'}

price = None
status = None

while True:
	#r = requests.post('https://api.exmo.com/v1.1/trades', headers = headers, data = data)
	

	#now_price = r.json()['BTC_USD'][0]['price']

	now_price = input('Ввод')

	if price == None and status == None:
		price = now_price
		status = 'Fix'
		print(f'Fix {price}')

	elif float(now_price) < float(price) * 0.99 and (status == 'Sell' or 'Fix') :

		price = now_price
		status = 'By'
		print(f'By {price}')

	elif float(now_price) > float(price) * 1.01 and status == 'By':
		price = now_price
		status = 'Sell'
		print(f'Sell {price}')

def statistic():
	pass

def get_balance():

	balance = None
	return balance



	print(price)
	sleep(5)




	

	



