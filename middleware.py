import requests, string, asyncio, time
from flask import Flask, jsonify
from threading import Thread

app = Flask(__name__)

@app.route('/mid/<name>', methods = ['GET','POST'])
def main(name):

    caixa, concat =  requests.post("http://127.0.0.1:5001/%s" % (name)), requests.post("http://127.0.0.1:5002/%s" % (name))
    
    return jsonify({
    	"Entrada": caixa.json()['enviado'],
        "Caixa Alta":  caixa.json()['resposta'],
        "Concatenado": concat.json()['resposta']
    })

if __name__ == '__main__':
    app.run(threaded = True, debug = True, host= 'localhost',  port = 4000)
