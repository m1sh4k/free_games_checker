import requests
from bs4 import BeautifulSoup



def check_steam():
    steam_connection_error = Exception()
    ok = True
    site = requests.Response()
    for i in range(3):
        site = requests.get('https://store.steampowered.com/search/?sort_by=_ASC&force_infinite=1&maxprice=free&supportedlang=english&snr=1_7_7_230_7&specials=1&page=1') 
        if site.status_code != 200:
            print(site, 'retrying...')
            ok = False
        else:
            ok = True
            break

    if not(ok):
        raise steam_connection_error
        

    soup = BeautifulSoup(site.text, 'html.parser')
    games = soup.find_all('span', class_='title')

    for i in range(len(games)):
        games[i] = games[i].text

    links = soup.find_all('a', class_='search_result_row ds_collapse_flag')

    for i in range(len(links)):
        links[i] =links[i]['href']

    return games, links


