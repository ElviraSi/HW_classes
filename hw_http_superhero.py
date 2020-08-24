import requests

def get_max_intel():
    """Получение информации о герое с максимальным интеллектом"""

    #список для теста
    # names = ['Hulk', 'Captain America', 'Thanos', 'Loki']

    #при тестировании закомментить строки 8-11
    name = input('Введите имена героев через запятую: ')
    names = []
    names.extend(name.split(', '))
    names_list = []

    for name in names:
        url = 'https://superheroapi.com/api/2619421814940190/search/'+name
        response = requests.get(url)
        result = response.json()
        names_list.append(result)
    heroes_list = []
    for hero in names_list:
        hero_name = hero['results-for']
        hero_result = hero['results']
        hero_id = int(hero_result[0]['id'])
        hero_intel = int(hero_result[0]['powerstats']['intelligence'])
        hero_list = [hero_name, hero_id, hero_intel]
        heroes_list.append(hero_list)
    intel_cur = 0
    intel_max = 0
    for element in heroes_list:
        intel_cur = element[2]
        if intel_cur > intel_max:
            intel_max = intel_cur
            name_max = element[0]
    print(f'У героя {name_max} максимальный интеллект - {intel_max}.')

get_max_intel()
