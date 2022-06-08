# ポケモンを検索する
# possible_poke 正解の可能性があるポケモンの配列
# input_poke 入力したポケモン
# answer_str 各文字が当たっているかどうかの文字列 (不正解: 0, 文字だけ正解: 1, 文字も位置も正解: 2)

# グラードンと入力して，グは文字も位置も当たっている，ラは文字は当たっているが位置は違う，他は当たっていない場合は
# input_poke → "グラードン"
# answer_str → "21000"
def pokemon_search(possible_poke, input_poke, answer_str):
    good_name = [] # 条件に合致するポケモンの配列
    for name in possible_poke:
        is_good = True # nameのポケモンは条件に合致するか
        for i in range(len(input_poke)):
            # input_pokeのi文字目が不正解の場合，
            # input_pokeのi文字目がinameに入っていたら条件に合致しない
            if answer_str[i] == "0":
                if input_poke[i] in name:
                    is_good = False
                    break

            # input_pokeのi文字目が文字だけ当たってて位置が違う場合，
            # input_pokeのi文字目がnameのi文字目に含まれているか，nameに入っていなければ条件に合致しない
            elif answer_str[i] == "1":
                if input_poke[i] == name[i] or input_poke[i] not in name:
                    is_good = False
                    break

            # input_pokeのi文字目が文字も位置も当たってる場合，
            # input_pokeのi文字目がnameのi文字目に含まれていなければ条件に合致しない
            elif answer_str[i] == "2":
                if input_poke[i] != name[i]:
                    is_good = False
                    break
                
        # もしnameのポケモンが条件に合致してたら条件に合致するポケモンの配列に追加する
        if is_good:
            good_name.append(name)
            
    # 条件に合致するポケモンの配列を返す
    return good_name