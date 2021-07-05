from typing import List

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.generic import View
from django.forms.models import model_to_dict

from .forms import SearchForm
from .models import Pokemon
from .utils import levenshtein_distance

POKEMONS_PER_PAGE = 10


def pokemon_filter(name: str, hp: int, defense: int, range_filter: dict, page: int, name_distance: int) -> List[dict]:
    """
    Filter pokemons from DB by query
    """
    pokemon_qs = Pokemon.objects.filter()

    if range_filter:
        pokemon_qs = pokemon_qs.filter(**range_filter)

    if hp:
        pokemon_qs = pokemon_qs.filter(hp=hp)

    if defense:
        pokemon_qs = pokemon_qs.filter(defense=defense)

    if name_distance and name:
        # search with levenshtein_distance
        pokemons = list()
        filtered_pokemons = pokemon_qs.all()
        for fp in filtered_pokemons:
            if levenshtein_distance(fp.name, name) <= name_distance:
                pokemons.append(fp)

        if page:
            pokemons = pokemons[(page - 1) * POKEMONS_PER_PAGE: page * POKEMONS_PER_PAGE]

    else:
        # standard sql search
        if name:
            pokemon_qs = pokemon_qs.filter(name__icontains=name)

        if page:
            paginator = Paginator(pokemon_qs, POKEMONS_PER_PAGE)
            pokemons = paginator.get_page(page)
        else:
            pokemons = pokemon_qs.all()

    result = list()
    for p in pokemons:
        serialized_model = model_to_dict(p)
        result.append(serialized_model)

    return result


class PokemonSearch(View):

    def get(self, request):
        form = SearchForm(request.GET)
        if form.is_valid():
            result = pokemon_filter(
                form.cleaned_data['name'],
                form.cleaned_data['hp'],
                form.cleaned_data['defense'],
                form.range_filters(),
                form.cleaned_data['page'],
                form.cleaned_data['name_distance'],
            )
            return JsonResponse(result, safe=False)
        return JsonResponse({'status': 'query wrong'}, status=400)
