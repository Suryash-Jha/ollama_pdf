# Ollama connection using python llama3.2

from flask import Flask, jsonify, request 
from langchain_ollama import OllamaLLM

app = Flask(__name__)
llm = OllamaLLM(model="llama3.2")

def getAiResponse(userInput):
    response = llm.invoke(userInput)
    return response

@app.route('/', methods = ['GET', 'POST']) 
def home(): 
    if(request.method == 'GET'): 
        data = "Suryash's Ollama running! Send POST requests with your query!"
    if(request.method == 'POST'):
        userInput= request.json
        data= getAiResponse(userInput['userInput'])
    return jsonify({'data': data}) 




if __name__ == '__main__': 
    app.run(debug = True) 