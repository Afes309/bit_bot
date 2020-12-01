import numpy as np
import requests
import matplotlib.pyplot as plt



fig, ax = plt.subplots()


def test():
	headers = {'Content-Type': 'application/x-www-form-urlencoded'}
	data = {'pair':'BTC_USD'}
	
	r = requests.post('https://api.exmo.com/v1.1/trades', headers = headers, data = data)
	

	#now_price = r.json()['BTC_USD'][0]['price']

	#for i in r.json()['BTC_USD']:
		#print(i)

	print(r.text)


y = [18025,18090,18200,18100,19000,19200,18990,18700]
x = [0,1,2,3,4,5,6,7]

y1 = 19200
x1 = 5

ax.plot(x,y)
ax.scatter(x1,y1)
ax.hlines(y1*0.99, x[0],x[-1] )
ax.hlines(y1*1.01, x[0],x[-1] )

ax.text(x1, y1+10, 'By',
        fontsize = 20)

ax.set(title = 'test')



if __name__ == '__main__':
	
	plt.show()
