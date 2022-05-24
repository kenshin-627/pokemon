import pandas as pd

def word_count(pokemon_name):
    pokemon_name_uniquie = ""
    for name in pokemon_name:
        name_uniquie = "".join(set(name))
        pokemon_name_uniquie += name_uniquie
    pd.set_option("display.max_rows", 100)
    print(pd.Series(list(pokemon_name_uniquie)).value_counts())