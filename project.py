import pip._vendor.requests as requests
import json, pprint
from collections import OrderedDict

class Pokemon:

    def __init__(self, name):
        self.name = name
        self.data = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(self.name)).json()



    def getAbilities(self):
        abilites = []
        data = self.data['abilities']


        for ability in data:

            abilites.append(ability['ability']['name'])
        
        return abilites



    def getInfo(self):
        info = OrderedDict()
        stats = OrderedDict()

        stats.update(
            Health = self.data['stats'][0]['base_stat'],
            Attack = self.data['stats'][1]['base_stat'],
            Defense = self.data['stats'][2]['base_stat'],
            Speed = self.data['stats'][5]['base_stat'],
            BaseXP = self.data['base_experience']
        )

        info.update(
            Name = self.name,
            Height = self.data['height'], 
            Weight = self.data['weight'],
            Type = self.data['types'][0]['type']['name'],
            Stats = stats
            )


        return info


class Pokedex:
    def __init__(self, size):
        self.pokeNames = []
        self.pokemon = []
        self.size = size
        self.data = requests.get('https://pokeapi.co/api/v2/pokemon?limit=' + str(self.size) + '&offset=' + str(range(200))).json()

    def generatePokemon(self):
        for pokemon in self.data['results']:
            self.pokeNames.append(pokemon['name'])

    def addToDex(self):
        for pokemon in self.pokeNames:
            self.pokemon.append(Pokemon(pokemon).getInfo())

    def showPokeDex(self):
        return self.pokemon




dex = Pokedex(30)
dex.generatePokemon()
dex.addToDex()

pprint.pprint(dex.showPokeDex())



