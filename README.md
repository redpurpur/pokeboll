# Pokemon's project


### Brief

Professor Oak is in trouble! A wild Blastoise wreaked havoc in the server room and destroyed every single machine. There are no backups - everything is lost! Professor Oak quickly scribbles down all the Pokémon from memory and hands them to you on a piece of paper. (`/Data/pokemon.csv`). Your task is to restore the Pokémon Database from that file and create a Pokémon API so that they’re never lost again.

## How to start

```
docker-compose up --build

docker-compose exec poke_web bash
python manage.py migrate
python manage.py load_dataset
```

After you can open http://localhost:1337/pokemon and see all pokemons in db.

## How to filter

You have one endpoint  http://localhost:1337/pokemon

You can filter by:

`name`, `hp` (`hp_min`, `hp_max`), `defense` (`defense_min`, `defense_max`), `page`



Also, you can use Levenshtein distance in filtering by name

You need to set GET-parameters: `name` and `name_distance`

`name_distance` is max Levenshtein distance between `name` and pokemon's name.

### Example

http://localhost:1337/pokemon

show everyone pokemon



http://localhost:1337/pokemon?page=2

show second page



http://localhost:1337/pokemon?page=2&hp_max=1000&name=b

show second page of pokemon's list with hp<= 1000 and with `b` in `name`



http://localhost:1337/pokemon?page=2&hp_max=1000&name=b

show second page of pokemon's list with `hp<= 1000` and with `b` in `name`



http://localhost:1337/pokemon?page=1&hp_max=1000&name=gol&name_distance=5

show first page of pokemon's list with `hp<= 1000` and with `gol` in `name` with Levenshtein distance equal or less than 5

