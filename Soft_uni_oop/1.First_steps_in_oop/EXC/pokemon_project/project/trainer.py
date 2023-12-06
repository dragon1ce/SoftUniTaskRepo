from typing import List
from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons: List[Pokemon] = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon.name in [f.name for f in self.pokemons]:
            return f"This pokemon is already caught"
        else:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        found_pokemon = None
        for p in self.pokemons:
            if p.name == pokemon_name:
                self.pokemons.remove(p)
                found_pokemon = True
                break
        if found_pokemon:
            return f"You have released {pokemon_name}"
        else:
            return f"Pokemon is not caught"

    def trainer_data(self):
        pokemon_names = []

        for obj in self.pokemons:
            pokemon_names.append(f"- {obj.pokemon_details()}")
        x = '\n'.join(pokemon_names)
        return f"Pokemon Trainer {self.name}\n" \
               f"Pokemon count {len(self.pokemons)}\n" \
               f"{x}"


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.trainer_data())
