# API Rest com Flask - Lore

Esta API fornece funcionalidades para gerenciar informações sobre "lore", como personagens, raças e descrições em um ambiente de fantasia. A implementação utiliza o Flask e bibliotecas auxiliares para criar uma API RESTful.

## Configuração do Ambiente

### Criar o Ambiente Virtual

Para criar um ambiente virtual, execute o seguinte comando:

```bash
python -m venv venv
Ativar o Ambiente Virtual
Para ativar o ambiente virtual, utilize:

bash
Copiar código
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
bash
Copiar código
venv/Scripts/activate
Desativar o Ambiente Virtual
Para desativar o ambiente virtual, execute:

bash
Copiar código
deactivate
Exportar a Lista de Dependências
Para exportar a lista de dependências para um arquivo requirements.txt, execute:

bash
Copiar código
pip freeze > requirements.txt
Instalar Dependências
Para instalar as dependências listadas no requirements.txt, execute:

bash
Copiar código
pip install -r requirements.txt
Instalar Bibliotecas Necessárias
Você também precisará instalar as seguintes bibliotecas:

bash
Copiar código
pip install flask-restful
pip install flask-pymongo
pip install flask-marshmallow
Executando o Servidor
No arquivo run.py, você pode configurar um exemplo inicial de Lore e executar o servidor. O código abaixo adiciona um lore padrão ao banco de dados, caso ele não exista:

python
Copiar código
from api import app, mongo
from api.models.lore_model import Lore  
from api.services.lore_service import LoreService  

if __name__ == '__main__':
    with app.app_context():
        if 'lore' not in mongo.db.list_collection_names():
            lore = Lore(
                name='Legolas',
                race='Elf',
                description={
                    "region": "Lothlórien",
                    "faction": "Elves of Lothlórien",
                    "important_battle": "Battle of Helm's Deep"
                }
            )
            LoreService.add_lore(lore)

    app.run(port=5000, debug=True)
Endpoints da API
Listar todos os lores
GET /lores
Retorna uma lista de todos os lores.

Criar um novo lore
POST /lores
Cria um novo lore. O corpo da requisição deve conter os seguintes campos:

name: Nome do personagem.
race: Raça do personagem.
description: Descrição em formato JSON que pode incluir campos como region, faction e important_battle.
Obter um lore por ID
GET /lore/<id>
Retorna os detalhes de um lore específico baseado no seu ID.

Atualizar um lore
PUT /lore/<id>
Atualiza um lore existente. O corpo da requisição deve conter os campos que deseja alterar.

Excluir um lore
DELETE /lore/<id>
Remove um lore específico do banco de dados.

Conclusão
Esta API fornece uma maneira robusta de gerenciar informações sobre personagens em um universo de fantasia. Com a utilização do Flask, Flask-Restful e outras bibliotecas, a implementação é simples e extensível para futuras adições de funcionalidades.


Agora está tudo organizado e estruturado para facilitar a leitura e compreensão. Se precisar de mais alguma modificação ou ajuste, é só avisar!
