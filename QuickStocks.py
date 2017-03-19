#Quick Stocks v.2
#Author: Hunter Barbella (aka hman523)
#Use: to have a command line interface for checking stocks
#This code uses the GPL licence while the API uses the MIT licience

#This code is provided AS IS and provides no warrenty

#Imports the libraries requests for making the GET request and 
#JSON for parsing the request
#sys and argparse for command line options
import requests
import json
import sys
import argparse



#This is the API URL that is used
emptyUrl = "http://dev.markitondemand.com/MODApis/Api/v2/Quote/jsonp?symbol="



#A nice welcome screen to print
def welcomePrint():
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
		  "\n\nVersion: 2.0	Author: Hunter Barbella (AKA hman523)\n\n"



	)

#Informs user how to leave program
print("To quit type quit or Control + \"c\"")

#calls the api and returns a nice string of the json
def callApi(stockSymbol):
	stockSymbol.upper()
	apiCall = requests.get(emptyUrl + stockSymbol)
	apiCall = str(apiCall.content)
	
	#Clean up the junk by gettin rid of the unneeded data
	indexOfStatus = apiCall.find('\"Status\"')
	length = len(apiCall)
	apiCall = apiCall[(indexOfStatus-1):length-2]
	return apiCall

#converts the string to a json file if it can, if not it returns none
def apiCallToJson(call):
	if(len(call) > 0):
		jsonOfCall = json.loads(call)
		return jsonOfCall
	else:
		return None

#prints all metadata from a given json
def printAllInfo(jsonOfCall):

	if(jsonOfCall is not None and jsonOfCall['Timestamp'] is not None):
		print("Firm- " + jsonOfCall['Name'])
		print("Symbol- " + jsonOfCall['Symbol'])
		print("Last Price- " + str(jsonOfCall['LastPrice']))
		print("Change- " + str(jsonOfCall['Change']))
		print("Percent Change- " + str(jsonOfCall['ChangePercent']) + "%")
		print("Time- " + str(jsonOfCall['Timestamp']))
		print("Market Cap- " + str(jsonOfCall['MarketCap']))
		print("Volume- " + str(jsonOfCall['Volume']))
		print("High- " + str(jsonOfCall['High']))
		print("Low- " + str(jsonOfCall['Low']))
		print("Open- " + str(jsonOfCall['Open']))
		print("Year To Date Change- " + str(jsonOfCall['ChangeYTD']))
		print("Year To Date Percent Change- " + str(jsonOfCall['ChangePercentYTD']) + "%")
		print("")
	else:
		error = "unknown error occured"

		if(jsonOfCall is None):
			error = "stock doesn't exist"
		else:
			if(jsonOfCall['LastPrice'] is 0 and jsonOfCall['MarketCap'] is 0):
				error = ("server error with stock " + jsonOfCall['Symbol'])
		
		print("Error occured: " + error + "\n")

#gets the user input and returns it, also checks if user quits program
def getUserInput():
	print("Enter a ticket symbol for a firm or load file:")
	userInput = input()
	if(userInput.lower() == 'quit'):
		quit()
	userInput = userInput.replace(" ", "")
	return userInput

#using a filename, this opens and returns stock info
def getStocksFromFile(stockFile):
	with open(stockFile) as f:
		listOfNames = f.readlines()
	listOfNames = [i.strip() for i in listOfNames]
	return listOfNames



	
	

#Main loop in the program
#Asks the user for a stock symbol and searches info based on that
def main():
	welcomePrint()

	descriptionString = """Arguments: -f -q
	f: file name
	q: quick lookup option
	"""

	parser = argparse.ArgumentParser(description=descriptionString)

	parser.add_argument('-sparams', nargs=1, dest='sparams', required=False,
		help="Use the argument -q or -f")



	while(True):
	


		#It gets the user inout, calls the api with it,
		# converts it to a JSON then it prints the data.
		userIn = getUserInput()
		if (userIn.startswith('load')):
			names = getStocksFromFile(userIn[4:])
			print("Reading from " + userIn[4:])
			for n in names:
				print("Reading...")
				printAllInfo(apiCallToJson(callApi(n)))
		else:
			printAllInfo(apiCallToJson(callApi(userIn)))


if __name__ == '__main__':
	main()