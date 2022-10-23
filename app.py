"""from cgitb import text
from concurrent.futures import process
from symbol import parameters
from flask import Flask,  request, make_response, json
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"



# create a route for webhook 
@app.route('/webhook', methods=[ 'POST']) 
def webhook(): 
    req=request.get_json(silent=True,force=True)
    fulfillmentText = ''
    query_result=req.get('queryResult')
    if query_result.get('action')=='get.address':
        
        fulfillmentText = "Hello"
    return{
        "fulfillmentText":fulfillmentText, "source": "webhookdata"
    }



@app.route('/webhook', methods=[ 'GET','POST'])
def webhook(): 

    if request.method == 'POST':
        req=request.get_json(silent=True,force=True)
        res=processRequest(req)

        res =json.dumps(res,indent=4)
        r=make_response(res)
        r.headers['Content-Type']='application/json'
        return r

def processRequest(req):

    query_response=req["queryResult"]
    print(query_response)
    text = query_response.get('queryText',None)
    parameters= query_response.get('parameters',None)
    res=get_data()
    return res

def get_data():
    data="Flask api"
    return{
        "fulfillmentText":data,
    }
# run the app 
if __name__ == '__main__': 
    app.debug=True
    app.run()"""

from flask import Flask, request
import json 
import random
import requests
app = Flask(__name__)
app.debug = True

@app.route('/')
def hello():
    return "Hello World"

@app.route('/',methods=['POST'])
def index():
    
    body = request.json
    city= body['queryResult']['parameters']['geo-city']
    
    
    appId = ''

    
    api_url='https://api.openweathermap.org/data/2.5/weather?q='+ city + '&units=metric&appid='+ appId
    headers = {'Content-Type': 'application/json'} 
    response = request.get(api_url, headers=headers) 
    r=response.json() 

    
    weather = str(r["weather"][0]["description"])
    temp = str(int(r['main']['temp']))
    humidity = str(r["main"]["humidity"])
    pressure = str(r["main"]["pressure"])  
    windSpeed = str(r["wind"]["speed"])
    windDirection = str(r["wind"]["deg"])
    country=str(r["sys"]["country"])
    #build the Dialogflow reply.
    reply = '{"fulfillmentMessages": [ {"text": {"text": ["Currently in '+ city + ', '+ country + ' it is ' + temp + ' degrees and ' + weather + '"] } } ]}'
    return reply