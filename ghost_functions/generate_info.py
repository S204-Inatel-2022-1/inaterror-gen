# C:\Users\Leolang\PycharmProjects\jsonfantasmas\venv\Lib\site-packages\qt5_applications\Qt\bin
import names
import random


class GenerateGhost:
    def __init__(self):
        self.ghost_name = self.generate_name()
        self.ghost_type = self.generate_type()
        self.ghost_location = self.generate_location()
        self.ghost_rarity = self.generate_rarity()

    def generate_name(self):
        return names.get_full_name()

    def generate_rarity(self):
        ghost_rarity = ["common", "uncommon", "rare", "epic", "legendary"]
        ghost_rarity = random.choices(ghost_rarity, weights=[50, 20, 10, 5, 1], k=1)
        return ghost_rarity[0]

    def generate_type(self):
        ghost_type = ["Banshee", "Demon", "Goryo", "Hantu", "Jinn", "Mare", "Myling", "Obake", "Oni", "Onryo",
                      "Phantom", "Poltergeist", "Raiju", "Revenant", "Shade", "Spirit", "The Twins", "Wraith", "Yurei",
                      "Yokai"]
        ghost_type = random.choice(ghost_type)
        return ghost_type

    def generate_location(self):
        ghost_location = "Insira aqui coordenadas do GPS"
        return ghost_location

    def print_info(self):
        print("Nome: {}".format(self.ghost_name))
        print("Tipo: {}".format(self.ghost_type))
        print("Localização: {}".format(self.ghost_location))
        print("Raridade: {}".format(self.ghost_rarity))
#ghost = GenerateGhost()
#print(ghost.print_info())
