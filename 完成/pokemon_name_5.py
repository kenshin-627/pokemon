import csv
import os
from pokemon_name import pokemon_name

def pokemon_name_5():
    pokemon_name = []
    if not os.path.isfile("pokemon_name.csv"):
        pokemon_name()
    with open("pokemon_name.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            pokemon_name = row

    pokemon_name_5 = []
    for name in pokemon_name:
        if len(name) == 5:
            pokemon_name_5.append(name)

    with open('pokemon_name_5.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(pokemon_name_5)