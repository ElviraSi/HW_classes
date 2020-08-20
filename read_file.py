from pprint import pprint
with open('recipes.txt', 'r', encoding='utf-8') as f:
    f_list = f.readlines()
    dish_list = []
    for elem in f_list:
        elem = elem.strip()
        if elem != '':
            dish_list.append(elem)
    dish_list = iter(dish_list)

keys = ['ingredient_name', 'quantity', 'measure']
cook_book = {}

for name in dish_list:
    cook_book[name] = []
    iter_num = next(dish_list)
    for _ in range(int(iter_num)):
        composition_line = next(dish_list)
        ingredient = composition_line.split(' | ')
        union = zip(keys, ingredient)
        composition_line = {k: v for (k, v) in union}
        cook_book[name].append(composition_line)
        continue
    continue

# pprint(cook_book, width=5, sort_dicts=False)

def get_shop_list_by_dishes():
    dishes_list = []
    dishes = input('Введите блюда через запятую без пробела: ')
    person_count = int(input('Введите количество персон: '))
    dishes_list.append(dishes)
    dishes_list = dishes.split(',')
    shop_list = []
    for dishes in dishes_list:
        for key, value in cook_book.items():
            if dishes == key:
                shop_list.extend(cook_book[dishes])
    shop_dict_all = {}
    for element in shop_list:
        for key, value in element.items():
            if key == 'ingredient_name':
                shop_dict = {value: {'measure': element['measure'], 'quantity': int(element['quantity'])*person_count}}
                shop_dict_all.update(shop_dict)
    return shop_dict_all

pprint(get_shop_list_by_dishes())