# Stream-Processing-Forex-Exchange-Market
This repository includes scripts to calculate and process on real time Forex exchange trading values. 

The main objective of this exercise is to produce a stream processing program that will obtain the data from a messaging system and will perform the pertinent calculations to feed an interface (not included in this repository) that will show the different Forex Exchange Trading values including a margin adjustment to each price (like commission).

## The Data
The data will consist of real time data extracted from yahoo finances webpage. It will consist of the price including a unique id, instrument name, bid, ask and timestamp. We will assume that the Bid means the sell price and the Ask is the buy price.

The market price feed will be given to you in CSV format line by line for EUR/USD, GBP/USD and EUR/JPY, e.g. here are some individual messages:

>106, EUR/USD, 1.1000,1.2000,01-06-2020 12:01:01:001

>107, EUR/JPY, 119.60,119.90,01-06-2020 12:01:02:002

>108, GBP/USD, 1.2500,1.2560,01-06-2020 12:01:02:002


## Scripts

This repository includes the files necessary to:
- Simulate a remote server with a messaging system feeding our own server with a stream of data line by line with different FX market values.
- A stream processing system receiving the data will then process it (adding the margin of -0.1% on bid, +0.1% on ask) and publish it to a REST endpoint where we can assume there will be an interface using the input to show it directly to the client.

## Graph
![alt text](https://github.com/Gares95/Stream-Processing-Forex-Exchange-Market/blob/main/Img/Diagram.png?raw=true)

# Requirements
For the _Client.py_ script to work it is necessary to install the library _bs4_ and _request_ to extract the ask and bid data from yahoo finance. 
You can use:
``pip install -r requirements.txt``

# Program files
## client.py

This first script serves to extract real time data from yahoo finances using bs4 and includes a messaging system to feed the server that will process the information. Using this script, we can use real time data instead of random values and we can simulate a stream of data to perform a stream processing instead of a batch processing which would be inefficient for a project like this.

## server.py

With this file we will process all the data and publish it to REST endpoint (as well as print it on screen to see the final results) 

## README.md

This file provides the description of the program and the stream processing.

## Test

To test this project it would only be necessary to run the client and the server on different terminal and it will be possible to see the real time output on the screen:
![alt text](https://github.com/Gares95/Stream-Processing-Forex-Exchange-Market/blob/main/Img/Testing.PNG?raw=true)



# Possible Future Scenarios
Using cloud services like AWS it would be possible to implement this program:  
- An EC2 machine running server.py and publishing the data to the right endpoint could work efficiently to get a real time analysis.
