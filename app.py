# Ollama connection using python llama3.2

from flask import Flask, jsonify, request 
from langchain_ollama import OllamaLLM
import time

app = Flask(__name__)
llm = OllamaLLM(model="llama3.2")

def getAiResponse(userInput):
    response = llm.invoke(userInput)
    return response

def getAiResponseFromDefaultServer(userInput):
    headers = {
        'Content-Type': 'application/json',
    }

    json_data = {
        'model': 'llama3.2',
        'prompt': userInput,
        'stream': False,
    }

    response = requests.post('http://127.0.0.1:11434/api/generate', headers=headers, json=json_data)
    details= response.json()
    return details['response']

@app.route('/', methods = ['GET', 'POST']) 
def faster(): 
    startTime= time.time()
    if(request.method == 'GET'): 
        data = "Suryash's Ollama running! Send POST requests with your query!"
    if(request.method == 'POST'):
        userInput= request.json
        data= getAiResponse(userInput['userInput'])
    endTime= time.time()
    totalTime= endTime- startTime
    return jsonify({'data': data, 'totalTcrate a navbar using mui joyime': totalTime}) 

import requests

@app.route('/original', methods = ['POST']) 
def home(): 
    startTime= time.time()
    if(request.method == 'POST'):
        userInput= request.json
        data= getAiResponseFromDefaultServer(userInput['userInput'])
    endTime= time.time()
    totalTime= endTime- startTime
    return jsonify({'data': data, 'totalTime': totalTime}) 

if __name__ == '__main__': 
    app.run(debug = True) 