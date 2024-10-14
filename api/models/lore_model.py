from api import mongo

class Lore:
    def __init__(self, name, race, description):
        self.name = name  # Nome do personagem
        self.race = race  # Raça do personagem
        self.description = description  # Documento aninhado
