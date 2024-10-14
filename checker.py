import requests
import json
from bs4 import BeautifulSoup


class game:
    title: str
    description: str
    link: str
    
    def __init__(self, title, description, link) -> None:
        self.title = title
        self.description = description
        self.link = link

    def build_message(self):
        return f'<strong>{self.title}</strong>\n\n{self.description}\n{self.link}'


def parse_egs() -> list[game]:
    games = []
    url = 'https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions?locale=ru&country=US&allowCountries=GB'
    game_url_prefix = 'https://store.epicgames.com/en-US/p/'
    site = requests.get(url)
    a = json.loads(site.text)
    
    for i in a['data']['Catalog']['searchStore']['elements']:
        if i['price']['totalPrice']['discountPrice'] == 0:
            games.append(game(i['title'], i['description'], game_url_prefix + i['offerMappings'][0]['pageSlug']))
    
    return games


def parse_steam() -> list[game]:
    games = []
    url = 'https://store.steampowered.com/search/?sort_by=_ASC&force_infinite=1&maxprice=free&supportedlang=english&snr=1_7_7_230_7&specials=1&page=1'
    site = requests.get(url)
    soup = BeautifulSoup(site.text, 'html.parser')
    titles = soup.find_all('span', class_='title')
    
    for i in range(len(titles)):
        titles[i] = titles[i].text
    links = soup.find_all('a', class_='search_result_row ds_collapse_flag')
    for i in range(len(links)):
        links[i] =links[i]['href']
    for i in range(len(links)):
        games.append(game(titles[i], '', links[i]))

    return games

def parse_gog() -> list[game]:
    games = []
    url = 'https://catalog.gog.com/v1/catalog?limit=48&price=between%3A0%2C0&order=desc%3Atrending&discounted=eq%3Atrue&productType=in%3Agame%2Cpack%2Cdlc%2Cextras&page=1&countryCode=RU&locale=ru-RU&currencyCode=RUB'
    site = requests.get(url)
    a = json.loads(site.text)
        
    for i in a['products']:
        games.append(game(i['title'], '', i['storeLink']))

    return games

