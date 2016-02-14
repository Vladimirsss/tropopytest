#from flask import Flask

#app = Flask(__name__)

#@app.route("/")
#def hello():
#    return "Hello World!!"

#if __name__ == "__main__":
#    app.run(debug=True,host='0.0.0.0')


import requests
from urllib.request import Request, urlopen
import json
import time


print("<<<start>>>")

myroomid = "Y2lzY29zcGFyazovL3VzL1JPT00vYjE4YzJlMjAtY2ZjMS0xMWU1LWJmY2YtZTE4YTBkMzMwYTg1"
sheaders = {
    "Authorization": "Bearer M2RkNzJjNGQtY2UwNS00NGJkLThiOTgtNmQ2Y2VjYzdjMDI0YWY3N2ZjZGEtYzUz",
    "Content-type": "application/json"}


requestURL="https://api.ciscospark.com/v1/messages"+"?"+"roomId="+str(myroomid)+"&"+"max=1"

responseString=requests.get(requestURL,headers=sheaders)

ro=responseString.json()

print("1> ", ro["items"][0]["text"])

