#Quick Stocks v.1
#Author: Hunter Barbella (aka hman523)
#Use: to have a command line interface for checking stocks
#This code uses the GPL licence while the API uses the MIT licience

#This code is provided AS IS and provides no warrenty

#Imports the libraries requests for making the GET request and 
#JSON for parsing the request
import requests
import json

#This is the API URL that is used
emptyUrl = "http://dev.markitondemand.com/MODApis/Api/v2/Quote/jsonp?symbol="

#A nice welcome screen to print
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

#Informs user how to leave program
print("To quit type quit or Control + \"c\"")

#Main loop in the program
#Asks the user for a stock symbol and searches info based on that



while(True):
	#Takes user input
	print("Enter a ticket symbol for a firm:")
	userInput = input()
	stockName = userInput
	stockName.upper()
	
	#Calls the API
	apiCall = requests.get(emptyUrl + stockName)
	
	#Gets rid of some of the junk taht comes back
	#TODO: make this a json file
	apiCall = str(apiCall.content)
	indexOfStatus = apiCall.find('\"Status\"')
	apiCall = apiCall[(indexOfStatus-2):]
	
	#Prints the resulting call TODO: remove this later
	print(apiCall)
	
	#Prints all metadata
	print("Firm- " + "")
	print("Symbol- " + "")
	print("Last Price- " + "")
	print("Change- " + "")
	print("Percent Change- " + "")
	print("Time- " + "")
	print("Market Cap- " + "")
	print("Volume- " + "")
	print("High- " + "")
	print("Low- " + "")
	print("Open- " + "")
	print("Year To Date Change- " + "")
	print("Year To Date Percent Change- " + "")
		