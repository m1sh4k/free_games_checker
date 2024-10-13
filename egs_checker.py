import requests
import json

def check_egs():
    url = 'https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions?locale=ru&country=US&allowCountries=GB'
    game_url_prefix = 'https://store.epicgames.com/en-US/p/'

    site = requests.get(url)

#print(site.text)
    a = json.loads(site.text)
#print(a['data']['Catalog']['searchStore']['elements'])
    games = []
    for i in a['data']['Catalog']['searchStore']['elements']:
        if i['price']['totalPrice']['discountPrice'] == 0:
            games.append([i['title'], i['description'] ,game_url_prefix + i['offerMappings'][0]['pageSlug'], i['keyImages'][0]['url']])
    return games
#print(games)
