from flask import Flask, jsonify
import string

app = Flask(__name__)

@app.route('/<name>', methods=['GET','POST'])
def main(name):
	print("O que foi recebido: ", name)
	data = {
		"enviado": name,
		"resposta": name.upper(),
    }
	print("O que será enviado: ", name.upper())
	return jsonify(data)

if __name__ == '__main__':
    app.run(debug = True, port = 5001)