from pastebin_api import post_new_paste
from poke_api import search_for_pokemon
import sys

def main():
    search_term = get_pokemon_name()
    pokemon_info = search_for_pokemon(search_term)
    if pokemon_info:
        title, body_text = get_paste_data(pokemon_info, search_term)
        paste_url = create_new_paste(title, body_text)
        print(f'URL of new paste: {paste_url}')

def get_pokemon_name():
    num_params = len(sys.argv) - 1
    if num_params > 0:
        return sys.argv[1].strip().lower()
    else:
        print("Error: Missing Pokémon name")
        sys.exit(1)

def get_paste_data(pokemon_info, search_term):
    name = pokemon_info['name'].capitalize()
    abilities = ['- ' + ability['ability']['name'] for ability in pokemon_info['abilities']]
    title = f"{name}'s Abilities"
    body_text = '\n'.join(abilities)
    return title, body_text

def create_new_paste(title, body_text):
    paste_url = post_new_paste(title, body_text, '1M', '0')
    return paste_url

if __name__ == '__main__':
    main()

