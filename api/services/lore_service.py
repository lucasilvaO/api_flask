from api import mongo
from ..models.lore_model import Lore  # Certifique-se de que a classe Lore está importada corretamente
from bson import ObjectId

class LoreService:
    # Função para cadastrar
    @staticmethod
    def add_lore(lore):
        result = mongo.db.lore.insert_one({
            'name': lore.name,  # Adicionando o campo name
            'race': lore.race,
            'description': lore.description  # Adicionando o campo description
        })
        # Retorna o lore inserido, usando o ID gerado
        return mongo.db.lore.find_one({'_id': ObjectId(result.inserted_id)})
        
    # Função para listar todos os lore
    @staticmethod
    def get_lores():  # Corrigido para plural
        return list(mongo.db.lore.find())
    
    # Função para listar um único lore
    @staticmethod
    def get_lore_by_id(id):
        return mongo.db.lore.find_one({'_id': ObjectId(id)})
    
    # Função para alterar um lore
    @staticmethod
    def update_lore(id, lore_data):
        # Atualiza o lore e retorna o documento atualizado
        updated_lore = mongo.db.lore.find_one_and_update(
            {'_id': ObjectId(id)},
            {'$set': {
                'race': lore_data.race,
                'description': lore_data.description,  # Adicionando o campo description
            }},
            return_document=True  # Garante que o documento retornado seja o atualizado
        )
        return updated_lore
    
    @staticmethod
    def delete_lore(id):
        mongo.db.lore.delete_one({'_id': ObjectId(id)})
