import requests

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    pokemon = search_for_pokemon('123')
    if pokemon is not None:
        print(f'Name: {pokemon["name"]}')
        print(f'ID: {pokemon["id"]}')
        return pokemon

def search_for_pokemon(search_term):
    """Gets the details of a pokemon from the Poke API

    Args:
        search_term (str): the name or ID of the pokemon to retrieve

    Returns:
        dict: a dictionary containing the pokemon's details, or None if the request failed
    """

    # set up the header parameters
    header_params = {
        'Accept': 'application/json'
    }

    # convert the search term to a string, remove leading/trailing whitespace, and convert to lowercase
    search_term = str(search_term).strip().lower()

    # construct the URL for the search term
    url = f'{POKE_API_URL}{search_term}/'

    # send the GET request to the Poke API
    print(f'Searching Poke API for "{search_term}"...', end='')
    resp_msg = requests.get(url, headers=header_params)

    if resp_msg.ok:
        print('success')
        pokemon_data = resp_msg.json()
        print(f'Retrieved data for Pokemon {pokemon_data["name"]}')
        return pokemon_data
    else:
        print('failed')
        print(f'Status code: {resp_msg.status_code} ({resp_msg.reason})')
        return None


if __name__ == '__main__':
    main()