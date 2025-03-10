#!usr/bin/python3

from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/login', methods=['POST'])
def login():
    data = request.json

    if not data or 'login' not in data or 'senha' not in data:
        return jsonify({'erro': 'Login e senha são obrigatórios'}), 400

    login = data['login']
    senha = data['senha']

    return jsonify({'login': login, 'senha': senha})

if __name__ == '__main__':
    app.run(debug=True)