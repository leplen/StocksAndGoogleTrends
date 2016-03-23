#!/usr/bin/python

import numpy as np
import Quandl
import pandas
import numpy as np
import os
import subprocess
import re
import glob
import datetime 
import pdb

APIkey='fZhrsAcJjKHzbQTtzEXf'
if(1): #Testing the quandl API
    testTicker='AAPL'
    Stockdata=Quandl.get("WIKI/"+testTicker+".2",authtoken=APIkey,trim_start="2004-04-21",trim_end="2004-04-30")
    #Stockdata=Quandl.get("WIKI/"+testTicker+".2",authtoken=APIkey,trim_start="2004-04-21",trim_end="2004-04-30",collapse="weekly")
    #print Stockdata


oneWeek=datetime.timedelta(days=7)
count=0
for csvFile in glob.glob("TrendsData/*.csv"):
    #Get stock ticker from CSV filename
    tickMatch=re.search("TrendsData/([A-Z]+).csv",csvFile)
    if tickMatch: 
        Ticker=tickMatch.group(1)
    
    currentFile=open(csvFile,'r')
    trendFreq=0 #initialize trendFreq
    for line in currentFile:
        #Match start date, end date, frequency 
        trendMatch=re.search("(\d{4}-\d{2}-\d{2})\s*-\s*(\d{4}-\d{2}-\d{2}),(\d+)",line)
        if trendMatch:
            tFp=trendFreq #previos trendFreq
            startDate=datetime.datetime.strptime(trendMatch.group(1),"%Y-%m-%d")
            endDate=datetime.datetime.strptime(trendMatch.group(2),"%Y-%m-%d")
            newDate=startDate.strftime("%Y-%m-%d")
#            endDate=trendMatch.group(2)
            trendFreq=float(trendMatch.group(3))

            ### Volatility in search vs. volatility in price
            if tFp>0 and trendFreq/tFp >2: #if search frequency doubled, see what's up
                sWindowStart=startDate-oneWeek
                sWindowEnd=endDate+oneWeek
                stockP=Quandl.get("WIKI/"+Ticker+".2",authtoken=APIkey,trim_start=sWindowStart.strftime("%Y-%m-%d"),trim_end=sWindowEnd.strftime("%Y-%m-%d"))
                signal=(stockP.max()-stockP.min() )/stockP.mean(0,1)
                print csvFile, newDate
#                print stockP
                print signal.to_string(), trendFreq/tFp 

         #   cross correlation: Is all attention good attention
 #           sWindowStart=endDate-datetime.timedelta(days=2)
  #          sWindowEnd=endDate
   #         pdb.set_trace()
    #        dayStockP=Quandl.get("WIKI/"+Ticker+".2",authtoken=APIkey,trim_start=sWindowStart.strftime("%Y-%m-%d"),trim_end=sWindowEnd.strftime("%Y-%m-%d"))
 #           count+=1


#    if(count>15):
  #      break

"""
I would really like to make it so that the dataframes don't have 
words in them






"""
