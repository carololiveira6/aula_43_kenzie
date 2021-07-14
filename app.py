from flask import Flask, jsonify, request
from http import HTTPStatus

# Caso queira utilizar Try Excepet com erros customizados
# from custom_errors import InvalidColumnFilter, NotFound, MissingArgs


app = Flask(__name__)

@app.route("/games")
def get_games():
    # Seu código aqui
    # request.args.get("name") // Utilize para pegar o arg name da url
    # request.args.get("column") // Utilize para pegar o arg column da url

    name = request.args.get('name')
    column = request.args.get('column')
    pass