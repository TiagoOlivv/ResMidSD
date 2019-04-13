from flask import Flask, jsonify
import string

app = Flask(__name__)

@app.route('/<name>', methods=['GET','POST'])
def main(name):
	print("O que foi recebido: ", name)
	data1 = {
		"enviado": name,
		"resposta": name.replace(" ",""),
    }
	print("O que será enviado: ", name.replace(" ",""))
	return jsonify(data1)

if __name__ == '__main__':
    app.run(debug = True, port = 5002)