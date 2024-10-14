from flask_restful import Resource
from api import api
from flask import make_response, jsonify, request
from ..schemas import lore_schema
from ..models import lore_model
from ..services.lore_service import LoreService

class LoreList(Resource):
    def get(self):
        lores = LoreService.get_lores()  # Altera o método para obter os lores
        lore_schema_instance = lore_schema.LoreSchema(many=True)
        return make_response(lore_schema_instance.jsonify(lores), 200)
    
    def post(self):
        lore_schema_instance = lore_schema.LoreSchema()
        validate = lore_schema_instance.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)  # BAD REQUEST
        else:
            # Captura todos os dados do json
            json_data = request.get_json()
            # Cria uma nova instância da classe Lore usando o desempacotamento
            new_lore = lore_model.Lore(
                name=json_data['name'],
                race=json_data['race'],
                description=json_data['description']  # Adicionando o campo description
            )
            result = LoreService.add_lore(new_lore)
            res = lore_schema_instance.jsonify(result)
            return make_response(res, 201)  # Created
        
class LoreDetails(Resource):
    def get(self, id):
        lore = LoreService.get_lore_by_id(id)
        if lore is None:
            # NOT FOUND
            return make_response(jsonify("Lore não encontrado."), 404)  # Mudado para 404
        lore_schema_instance = lore_schema.LoreSchema()
        return make_response(lore_schema_instance.jsonify(lore), 200)  # OK
    
    def put(self, id):
        lore_bd = LoreService.get_lore_by_id(id)
        if lore_bd is None:
            return make_response(jsonify("Lore não foi encontrado."), 404)  # NOT FOUND
        lore_schema_instance = lore_schema.LoreSchema()
        validate = lore_schema_instance.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            json_data = request.get_json()
            updated_lore = lore_model.Lore(
                name=json_data['name'],
                race=json_data['race'],
                description=json_data['description']  # Adicionando o campo description
            )
            updated_lore = LoreService.update_lore(id, updated_lore)  # Corrigido para passar o id
            return make_response(lore_schema_instance.jsonify(updated_lore), 200)
        
    def delete(self, id):
        lore_bd = LoreService.get_lore_by_id(id)
        if lore_bd is None:
            return make_response(jsonify("Lore não encontrado."), 404)
        LoreService.delete_lore(id)
        return make_response(jsonify("Lore excluído com sucesso!"), 200)  # OK

api.add_resource(LoreList, '/lores')  # Altera para /lores
api.add_resource(LoreDetails, '/lore/<id>')  # Altera para /lore/<id>
