import requests, string, asyncio, time
from flask import Flask, jsonify
from threading import Thread

app = Flask(__name__)

@app.route('/mid/<name>', methods = ['GET','POST'])
def main(name):

    caixa, concat =  requests.post("http://127.0.0.1:5001/%s" % (name)), requests.post("http://127.0.0.1:5002/%s" % (name))
    
    return jsonify({
        "caixa":  caixa.json()['response'],
        "concat": concat.json()['response']
    })

if __name__ == '__main__':
    app.run(threaded = True, debug = True,host= '192.168.43.179',  port = 4000)
