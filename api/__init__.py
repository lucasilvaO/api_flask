from flask import Flask
from flask_restful import Api
from flask_pymongo import PyMongo
from flask_marshmallow import Marshmallow

# Criando a instância do Flask
app = Flask(__name__)

# Definindo o endereço do banco (local ou Atlas)
# Para conectar ao MongoDB Atlas, use a linha abaixo e substitua pelas suas credenciais
# app.config["MONGO_URI"] = "mongodb+srv://123zebob321:zebob123@cluster0.uil4p.mongodb.net/api_loreLTHR?retryWrites=true&w=majority"'

# Para conectar ao MongoDB local
app.config["MONGO_URI"] = 'mongodb://localhost:27017/api_loreLTHR'

# Criando a instância de Api do flask_restful e passando o Flask
api = Api(app)

# Criando a instância do PyMongo
mongo = PyMongo(app)

# Criando a instância do Marshmallow
ma = Marshmallow(app)

# Importando os recursos (certifique-se de que o caminho está correto)
from .resources import lore_resource
