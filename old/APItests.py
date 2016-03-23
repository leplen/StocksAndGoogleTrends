#!/usr/bin/python
"""
This is just testing the API and getting and setting up the data files

"""
import Quandl
import pandas
import numpy as np
import os
import subprocess
import re
import time
from random import randint
import glob

APIfile=open('Quandl.secret','r')
APIkey=APIfile.readline().strip()


if(1): #Testing the quandl API
    Ticker='AAPL'
    Stockdata=Quandl.get("WIKI/"+Ticker+".2",authtoken=APIkey,trim_start="2005-12-31",trim_end="2015-12-31",collapse="weekly")
    print Stockdata
def getCSV(SearchTerm): 
#This isn't super well done and isn't portable. It relies on telling firefox to 
#download files into a TrendsData folder and uses an addon called TabMixPlus prevent firefox
#from opening blank tabs for each download
    downloadLink='http://www.google.com/trends/trendsReport?q='+SearchTerm+'&hl=en-US&cmpt=q&content=1&export=1'
    subprocess.call(["firefox", downloadLink])

if(0): #Downloads google trends data for various ticker symbols
    tickerFile=open('WIKI_tickers.csv', 'r')
    for line in tickerFile:
        m=re.search('WIKI/([A-Z]+)',line)
        if m:
           tickerSymbol=m.group(1)
           fileCheck='TrendsData/'+tickerSymbol+'.csv'
           gotten=os.path.isfile('TrendsData/'+tickerSymbol+'.csv')
           if not (gotten): #don't redownload things
               time.sleep(randint(1,5)) #Possibly helps not getting identified as bot
               getCSV(tickerSymbol)  

if(0): #Downloaded files are named report(#).csv by default, which isn't convenient. 
#This just renames them so each csv file is named for the search term 
    for csvFile in glob.glob("TrendsData/repo*.csv"):
        currentFile=open(csvFile,'r')
        line1=currentFile.readline()
        m=re.search('Web Search interest: ([a-z]+)',line1)
        if m:
            csvFilemod=csvFile.replace('(','\\(').replace(')','\\)')
            ticker=m.group(1)
            renameComm='mv '+csvFilemod+' TrendsData/'+ticker.upper()+'.csv'
            os.system(renameComm)
