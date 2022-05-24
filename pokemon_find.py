def pokemon_find(pokemon_name, word_in, word_not):
    word_in = "".join(word_in)
    word_not = "".join(word_not)
    good_name = []
    for name in pokemon_name:
        is_good = True
        for i in word_in:
            if i not in name:
                is_good = False
        for i in word_not:
            if i in name:
                is_good = False
        if is_good:
            good_name.append(name)
#      word_inの文字が入ってて，word_notの文字が入っていないポケモンの配列を返す
    return good_name