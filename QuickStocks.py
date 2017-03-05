#Quick Stocks v.1
#Author: Hunter Barbella (aka hman523)
#Use: to have a command line interface for checking stocks
#This code uses the GPL licence while the API uses the MIT licience

#This code is provided AS IS and provides no warrenty


import requests
import json

emptyUrl = "http://dev.markitondemand.com/MODApis/Api/v2/Quote/jsonp?symbol="


print("  /$$$$$$            /$$           /$$                     \n" +
	  " /$$__  $$          |__/          | $$                     \n" +
	  "| $$  \ $$ /$$   /$$ /$$  /$$$$$$$| $$   /$$               \n" + 
	  "| $$  | $$| $$  | $$| $$ /$$_____/| $$  /$$/               \n" + 
	  "| $$  | $$| $$  | $$| $$| $$      | $$$$$$/                \n" + 
	  "| $$/$$ $$| $$  | $$| $$| $$      | $$_  $$                \n" + 
	  "|  $$$$$$/|  $$$$$$/| $$|  $$$$$$$| $$ \  $$               \n" +
	  " \____ $$$ \______/ |__/ \_______/|__/  \__/               \n" +
	  "      \__/                                                 \n" +
	  "                                                           \n" +
	  "                                                           \n" +
	  "  /$$$$$$   /$$                         /$$                \n" +
	  " /$$__  $$ | $$                        | $$                \n" +
	  "| $$  \__//$$$$$$    /$$$$$$   /$$$$$$$| $$   /$$  /$$$$$$$\n" +
	  "|  $$$$$$|_  $$_/   /$$__  $$ /$$_____/| $$  /$$/ /$$_____/\n" +
	  " \____  $$ | $$    | $$  \ $$| $$      | $$$$$$/ |  $$$$$$ \n" +
	  " /$$  \ $$ | $$ /$$| $$  | $$| $$      | $$_  $$  \____  $$\n" +
	  "|  $$$$$$/ |  $$$$/|  $$$$$$/|  $$$$$$$| $$ \  $$ /$$$$$$$/\n" +
	  " \______/   \___/   \______/  \_______/|__/  \__/|_______/ \n" +
	  "\n\nVersion: 1.0	Author: Hunter Barbella (AKA hman523)"



	)


while(True):
	print("Enter a ticket symbol for a firm:")
	userInput = input()
	stockName = userInput
	stockName.upper()
	apiCall = requests.get(emptyUrl + stockName)

	apiCall = str(apiCall.content)
	indexOfStatus = apiCall.find('\"Status\"')
	apiCall = apiCall[(indexOfStatus-2):]
	print(apiCall)
	

	count = 0
	stockMetadata = []
	while(count < len(apiCall)):
		count = count + 1
	print("Firm- " + "")