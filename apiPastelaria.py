from flask import Flask
from flask_restful import Api
from FuncionarioDAO import Funcionario
from ClienteDAO import Cliente

app = Flask(__name__)
api = Api(app)

# mapeamento dos endpoints
api.add_resource(Funcionario, "/funcionario/<int:id>", endpoint = 'funcionario')

api.add_resource(Cliente, "/cliente/<int:id>", endpoint = 'cliente')

if __name__ == "__main__":
    """ Inicia a API Flask RESTful """
    app.run(host='0.0.0.0', port=5000, debug=True)