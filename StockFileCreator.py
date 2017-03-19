#Quick Stocks v.2
#Author: Hunter Barbella (aka hman523)
#Use: to have a command line interface for checking stocks
#This code uses the GPL licence while the API uses the MIT licience

#This code is provided AS IS and provides no warrenty

#This program is a utility for QuickStocks
#Purpose: to create files with verified working stocks

import requests

emptyUrl = "http://dev.markitondemand.com/MODApis/Api/v2/Quote/jsonp?symbol="

def getUserInput():
	userInput = input()
	if(userInput.lower() == 'quit'):
		quit()
	return userInput

def callApi(stockSymbol):
	stockSymbol.upper()
	apiCall = requests.get(emptyUrl + stockSymbol)
	apiCall = str(apiCall.content)
	
	#Clean up the junk by gettin rid of the unneeded data
	indexOfStatus = apiCall.find('\"Status\"')
	length = len(apiCall)
	apiCall = apiCall[(indexOfStatus-1):length-2]
	if(len(apiCall) > 0):
		jsonOfCall = json.loads(apiCall)
		return jsonOfCall
	else:
		return None

print("Welcome to StockFileCreator!")
print("File Name?")
f = open(getUserInput(), 'a')

print("Stocks to add? (Put a space in between each one)")
userInput = getUserInput()
#jsonOfCall['LastPrice'] is 0 and jsonOfCall['MarketCap'] is 0
#jsonOfCall is None
words = userInput.split()
for stock in words:
	call = callApi(userInput)
	if (call is not None and (call['LastPrice'] is not 0 and call['MarketCap'] is not 0)):
		f.write(call['Symbol'])
		print("Wrote " + stock + "to file")
	else:
		print("Error with stock name " + stock)
f.close()
