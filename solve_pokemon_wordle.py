import csv
import os
from pokemon_name_5 import pokemon_name_5
from pokemon_search import pokemon_search
import sys

if __name__ == "__main__":
    # 5文字のポケモンの名前とってくる
    pokemon_name_5 = []
    if not os.path.isfile("pokemon_name_5.csv"):
        pokemon_name_5()
    with open("pokemon_name_5.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            pokemon_name_5 = row
        
    # 正解の可能性があるポケモン
    possible_poke = pokemon_name_5
    
    while(True):
        # 正解の可能性があるポケモンがおらんくなったら終了
        if len(possible_poke) == 0:
            print("ダイパまでにそんな名前の5文字のポケモンおらんで")
            print("なんか入力間違えてるはず")
            sys.exit(0)
        
        print("正解の可能性があるポケモン: " + str(len(possible_poke)) + "匹")
        
        # 正解の可能性があるポケモンが10匹以下なら全て表示する
        if len(possible_poke) <= 10:
            print(possible_poke)
        
        # 改行
        print()
        
        # 正解の可能性があるポケモンの中で誰を入力すれば全外しした時に正解の可能性があるポケモンの数が少なくなるか
        min_name = possible_poke[0]
        all_miss_min = len(pokemon_search(possible_poke, possible_poke[0], "00000"))
        for name in possible_poke:
            all_miss = len(pokemon_search(possible_poke, name, "00000"))
            if all_miss_min > all_miss:
                min_name = name
                all_miss_min = all_miss
        print("次に入力するおすすめのポケモン: " + min_name)
        
        # 改行
        print()
        
        # 入力と正誤を聞く
        print("あなたが入力したポケモンは: ")
        input_poke = input()
        
        # 改行
        print()
        
        print("返ってきた正誤は: (無色: 0, 黄色: 1, 緑色: 2)")
        answer_str = input()
        
        # 改行
        print()
        
        # 正解なら終了
        if answer_str == "22222":
            print("正解おめでとう！！")
            sys.exit(0)
        
        # 間違いなら入力から正解の可能性があるポケモンを探す
        possible_poke = pokemon_search(possible_poke, input_poke, answer_str)