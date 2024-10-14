from api import mongo
from ..models.lore_model import Lore
from bson import ObjectId

class LoreService:
    @staticmethod
    def add_lore(lore):
        result = mongo.db.lore.insert_one({
            'name': lore.name,
            'race': lore.race,
            'description': lore.description
        })
        return mongo.db.lore.find_one({'_id': ObjectId(result.inserted_id)})

    @staticmethod
    def get_lores():
        return list(mongo.db.lore.find())
    
    @staticmethod
    def get_lore_by_id(id):
        return mongo.db.lore.find_one({'_id': ObjectId(id)})
    
    @staticmethod
    def update_lore(id, lore_data):
        updated_lore = mongo.db.lore.find_one_and_update(
            {'_id': ObjectId(id)},
            {'$set': {
                'race': lore_data.race,
                'description': lore_data.description,
            }},
            return_document=True
        )
        return updated_lore
    
    @staticmethod
    def delete_lore(id):
        mongo.db.lore.delete_one({'_id': ObjectId(id)})
