import json
import collections

with open("newsafr.json", "r", encoding="utf-8") as f:
    reader = json.load(f)
    r_list = reader['rss']['channel']['items']
    words_list = []
    for r_elem in r_list:
        l = r_elem['description']
        words_list.extend(l.split())
    words_list = [x.lower() for x in words_list]
    words_list_upd = []
    for i in words_list:
        if len(i) > 6:
            words_list_upd.append(i)
    count_w = collections.Counter(words_list_upd).most_common(10)
    print(count_w)
