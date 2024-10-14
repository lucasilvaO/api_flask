from api import app, mongo
from api.models.lore_model import Lore  
from api.services.lore_service import LoreService  


if __name__ == '__main__':
   
    with app.app_context():
        if 'lore' not in mongo.db.list_collection_names():
            
            lore = Lore(
                name='Legolas',  # Nome do personagem
                race='Elf',  # Raça do personagem
                description={  # Documento aninhado
                    "region": "Lothlórien",  # Região onde vivem
                    "faction": "Elves of Lothlórien",  # Facção do personagem
                    "important_battle": "Battle of Helm's Deep"  # Batalha importante
                }
            )
           
            LoreService.add_lore(lore)

    app.run(port=5000, debug=True)
