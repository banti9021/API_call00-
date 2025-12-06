import requests

def fetch_pokemon():
    name = input("Enter Pokémon name: ").lower()

    url = f"https://pokeapi.co/api/v2/pokemon/{name}"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        data = response.json()

        print("Name:", data["name"])
        print("Height:", data["height"])
        print("Weight:", data["weight"])

        print("Abilities:")
        for ability in data["abilities"]:
            print("-", ability["ability"]["name"])

    except requests.exceptions.HTTPError:
        print("Pokémon not found! Please check the name.")
    except Exception as e:
        print("Error:", e)

fetch_pokemon()
