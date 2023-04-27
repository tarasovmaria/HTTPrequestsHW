from pprint import pprint

import requests

def the_smartest_hero(heroes_list):
    url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
    all_heroes = requests.get(url=url)
    heroes_intell = {}
    for hero in all_heroes.json():
        if hero['name'] in heroes_list:
            heroes_intell[hero['name']] = hero['powerstats']['intelligence']
        else:
            pass
    return f'Самый умный из суперов: {max(heroes_intell, key=heroes_intell.get)}'

if __name__ == '__main__':
    pprint(the_smartest_hero(['Hulk', 'Captain America', 'Thanos']))
