import csv

from django.core.management.base import BaseCommand
from django.conf import settings

from api.models import Pokemon


class Command(BaseCommand):
    help = "Load pokemons from CSV"

    def handle(self, *args, **options):
        pokemons_for_save = list()
        with open(settings.DATASET_FILE) as fh:
            reader = csv.DictReader(fh)

            for raw_pokemon in reader:
                if raw_pokemon.get('Legendary').capitalize() != 'False':
                    continue

                if raw_pokemon.get('Type 1', '').capitalize() == 'Ghost':
                    continue

                pokemon = Pokemon(
                    name=raw_pokemon.get('Name', '').capitalize(),
                    type1=raw_pokemon.get('Type 1', '').capitalize(),
                    type2=raw_pokemon.get('Type 2', '').capitalize(),
                    total=int(raw_pokemon.get('Total')),
                    hp=int(raw_pokemon.get('HP')),
                    attack=int(raw_pokemon.get('Attack')),
                    defense=int(raw_pokemon.get('Defense')),
                    special_attack=int(raw_pokemon.get('Sp. Atk')),
                    special_speed=int(raw_pokemon.get('Sp. Def')),
                    speed=int(raw_pokemon.get('Speed')),
                    generation=int(raw_pokemon.get('Generation')),
                )

                if pokemon.type1 == 'Steel' or pokemon.type2 == 'Steel':
                    pokemon.hp = pokemon.hp * 2

                if pokemon.type1 == 'Fire' or pokemon.type2 == 'Fire':
                    pokemon.attack = pokemon.attack - round(pokemon.attack / 10)

                if pokemon.type1 == 'Bug' and pokemon.type2 == 'Flying' or \
                        pokemon.type1 == 'Flying' and pokemon.type2 == 'Bug':
                    pokemon.speed = round(pokemon.speed * 1.1)

                if pokemon.name.startswith('G'):
                    name_set = set(pokemon.name.lower()) - set('g')
                    pokemon.defense = pokemon.defense + 5 * len(name_set)

                pokemons_for_save.append(pokemon)

        Pokemon.objects.bulk_create(pokemons_for_save)
        print('dataset loaded')
