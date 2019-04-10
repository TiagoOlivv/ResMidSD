from flask import Flask, jsonify
import string

app = Flask(__name__)

@app.route('/<name>', methods=['GET','POST'])
def main(name):
    print(">>>>", name)
    data = {
        "sended": name,
        "response": name.upper(),
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug = True, port = 5001)
