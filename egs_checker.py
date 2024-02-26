import requests
import json

link = 'https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions?locale=en-US&country=GB&allowCountries=GB'

site = requests.get(link)

#print(site.text)

a = json.loads(site.text)
#print(a['data']['Catalog']['searchStore']['elements'])
games = []
for i in a['data']['Catalog']['searchStore']['elements']:
    games.append(i['title'])

print(games)
