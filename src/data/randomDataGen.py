import urllib.request
import requests
import threading
import json

import random


# Define a function that will send random number to thingspeak every 15 Seconds (15 seconds with free license)

def thingspeak_post():
    threading.Timer(15,thingspeak_post).start()
    val=random.randint(1,30)
    URl='https://api.thingspeak.com/update?api_key='
    KEY='YU3PZWX7CYRBAZ2T'
    HEADER='&field1={}&field2={}'.format(val,val)
    NEW_URL=URl+KEY+HEADER
    print(NEW_URL)
    data=urllib.request.urlopen(NEW_URL)
    print(data)

def read_data_thingspeak():
    #If you want more data then just change the ending of the URL below to something greater than 1
    URL='https://api.thingspeak.com/channels/1623608/fields/1.json?api_key=5F0TNMB5TYYI54BY&results=1' 
    data=requests.get(URL).json()
    print(data)
if __name__ == '__main__':
    #thingspeak_post()
    read_data_thingspeak()

