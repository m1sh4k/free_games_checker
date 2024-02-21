import requests
from bs4 import BeautifulSoup



def check_steam():
    site = requests.Response()
    for i in range(3):
        try:
            site = requests.get('https://store.steampowered.com/search/?sort_by=_ASC&force_infinite=1&maxprice=free&supportedlang=english&snr=1_7_7_230_7&specials=1&page=1') 
            break
        except:
            continue

    print(site)

    soup = BeautifulSoup(site.text, 'html.parser')
    games = soup.find_all('span', class_='title')

    for i in range(len(games)):
        games[i] = games[i].text

    links = soup.find_all('a', class_='search_result_row ds_collapse_flag')

    for i in range(len(links)):
        links[i] =links[i]['href']

    return games, links


print(check_steam())
