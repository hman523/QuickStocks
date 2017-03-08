# QuickStocks
A quick command line tool to search stock info

This program is in version 2.0.

##Use
This program provides no warrenty and is provided AS IS.
This program uses the GPL v.3 while the API uses the MIT licence.  Use these responsibly.
It is not recommended that one would use this data to view stock info in real time for finacial purposes.  This is more suited for general quick browsing of metadata.  For more in depth info one should use a stock broker.  

##Instructions
To search for stock metadata, type in the symbol for the stock. There is a bug where some stocks will return no data but the name of the company.  This is a known error and is rare.  It appears to be server side so it is out of my control.
To quit the program, type quit, case insensitive.  You can also use CTRL + "c" to keyboard interupt the program but it might not work well if you are writing to a file at the time of exiting.  
The new update I worked on allows for files to be used.  A new script was written to create the files to use.

##Future releases
I plan to add the ability to add files to save stock names in a files so you can print multiple stocks at once.  Another feature I wish to add is the ability to use command line options to use quick results.

##Hopes and dreams for this project
The goal of this is for me to work with Python, a language I have not loved so much in the past.  By forcing myself to do this, I actually have started to enjoy the succinct nature of the language.
I also want for this program to be usable in bash scripts to link somethingusing stock data, ie. a CRON script that runs this api, checks its output and does an action if something happens.
