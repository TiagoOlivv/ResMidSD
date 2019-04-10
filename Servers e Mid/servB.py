from flask import Flask, jsonify
import string

app = Flask(__name__)

@app.route('/<name>', methods=['GET','POST'])
def main(name):
	print(">>>>", name)
	data1 = {
		"sended": name,
		"response": name.replace(" ",""),
    }
	return jsonify(data1)

if __name__ == '__main__':
    app.run(debug = True, port = 5002)