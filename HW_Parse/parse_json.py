import json

with open("newsafr.json", "r", encoding="utf-8") as f:
    reader = json.load(f)
    r_list = reader['rss']['channel']['items']
    words_list = []
    for r_elem in r_list:
        l = r_elem['description']
        words_list.extend(l.split())
    words_list_upd = []
    for i in words_list:
        if len(i) >= 6:
            words_list_upd.append(i)
    words_dict = {}.fromkeys(words_list_upd, 0)
    for word in words_list_upd:
        words_dict[word] += 1
    words_dict_upd = {}
    for key, value in words_dict.items():
        words_dict_upd[value] = key
    for k in sorted(words_dict_upd.keys(), reverse=True)[:10]:
        if k % 10 == 2 or k % 10 == 3 or k % 10 == 4:
            print(f'Слово "{words_dict_upd[k]}" повторяется {k} раза.')
        else:
            print(f'Слово "{words_dict_upd[k]}" повторяется {k} раз.')