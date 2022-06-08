import requests
import csv

def pokemon_name():
    pokemon_name = []
    # ポケモン図鑑495番まで(ダイヤモンド・パールまで）のポケモンの名前情報(日本語)を取得
    for i in range(1,495):
        url = "https://pokeapi.co/api/v2/pokemon-species/" + str (i)
        response = requests.get(url)
        pokemon_data = response.json()
        pokemon_name.append(pokemon_data["names"][0]["name"])
        
    # チョンチーとブニャットだけ["names"][0]が日本語じゃなかったから手動で書き直す
    pokemon_name[169] = "チョンチー"
    pokemon_name[431] = "ブニャット"
    with open('pokemon_name.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(pokemon_name)