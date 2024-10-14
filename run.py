from api import app, mongo
from api.models.lore_model import Lore  # Verifique se a classe Lore está definida corretamente
from api.services.lore_service import LoreService  # Verifique se o método add_lore está implementado

# Iniciando a aplicação com modo de depuração ativo
if __name__ == '__main__':
    # Criando o banco e a coleção se não existir
    with app.app_context():
        if 'lore' not in mongo.db.list_collection_names():
            # Atualizando para a nova estrutura
            lore = Lore(
                name='Legolas',  # Nome do personagem
                race='Elf',  # Raça do personagem
                description={  # Documento aninhado
                    "region": "Lothlórien",  # Região onde vivem
                    "faction": "Elves of Lothlórien",  # Facção do personagem
                    "important_battle": "Battle of Helm's Deep"  # Batalha importante
                }
            )
            # Usando o serviço para adicionar o 'lore'
            LoreService.add_lore(lore)

    app.run(port=5000, debug=True)
