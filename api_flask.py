from flask import Flask, jsonify, request
import json
import pandas as pd
from flask_ngrok import run_with_ngrok
import threading
from time import sleep


df = pd.read_excel('base_api.xlsx')

df.to_json('base_json.json')


dados_json = json.loads(open('base_json.json').read())

app = Flask(__name__)
run_with_ngrok(app)

@app.route('/')
def hello():
    return 'Hello, world!'

@app.route('/output', methods=['GET', 'POST'])
def out():
  return jsonify(dados_json)

def start_ngrok():
    from pyngrok import ngrok
    ngrok.connect(5000)

if __name__ == '__main__':
    ngrok_thread = threading.Thread(target=start_ngrok)
    ngrok_thread.start()
    app.run()