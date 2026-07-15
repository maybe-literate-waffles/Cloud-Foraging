import requests
import datetime as dt
import time as tm

# base_url = "https://pokeapi.co/api/v2/"


# def fetch_poke_info(poke_name):
#     url = f"{base_url}/pokemon/{poke_name}"
#     response = requests.get(url)

#     if response.status_code == 200:
#         poke_data = response.json()
#         return poke_data
#     else:
#         print(f"Error: {response.status_code}")


# def poke_details(poke_info):
#     print(f"Name: {poke_info['name']}")
#     print(f"Ability: {poke_info['abilities'][0]['ability']['name']}")
#     # print(f"Total bst: {poke_info['']}")
#     # print(f"Name: {poke_info['name']}")
#     pass


# poke_name = input("Search: ")

# poke_info = fetch_poke_info(poke_name)
# poke_details(poke_info)

time = dt.datetime.now()

print(time)

# print(f"Ability: {poke_info['abilities'][0]['ability']['name']}")
