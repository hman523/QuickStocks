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
stockName = "t"
stockName.upper()
apiCall = requests.get(emptyUrl + stockName)

apiCall = str(apiCall.content)
indexOfStatus = apiCall.find('\"Status\"')
apiCall = apiCall[(indexOfStatus-2):]
json.dumps(apiCall)
print("Firm: " + "")


print(apiCall)
#while(true):
#	userInput = input()