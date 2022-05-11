import random
import requests
from bs4 import BeautifulSoup


def pobranie_strony(wybor):

    headers = {'User_Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0'}
    if wybor:
        wyszukaj = f'https://rozrywka.ox.pl/{wybor}?orderBy=1'
    else:
        wyszukaj = f'https://rozrywka.ox.pl/humor?orderBy=1'

    r = requests.get(wyszukaj, headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    return soup


def pob_st():

    headers = {'User_Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0'}

    wyszukaj = f'https://rozrywka.ox.pl/humor?orderBy=1'
    r = requests.get(wyszukaj, headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    return soup


def losowy_zart(soup):
    jeden_zart = []

    x = pob_st()
    zarcik = x.find_all('p')

    for zar in zarcik:
        zar.find('p')
        zarr = str(zar.text).replace('\t', '').replace('\n', '')
        jeden_zart.append(zarr)

    x = jeden_zart[random.randrange(0, 20, 1)]

    return x


def losowe_wykonanie():
    y = pob_st()
    z = losowy_zart(y)
    return z


def zarty_kategorie(soup):
    kategorie = []
    licznik = 0
    zarty = soup.find_all('div', class_='newNotice__categoryRow')
    for zart in zarty:
        if licznik < 5:
            zart = zart.text

            zart = 'Posiadam bazę danych żartów o tematyce: ' + (str(zart).replace('\n\n', '').replace('    ', '')).replace('\n', '').replace(' ', ',')
            kategorie.append(zart)
            licznik += 1
        else:
            break
        break

    return kategorie


def zarty_wykonanie(wybor):
    jeden_zart = []
    if wybor:
        x = pobranie_strony(wybor)
        zarcik = x.find_all('p')

        for zar in zarcik:
            zar.find('p')
            zarr = str(zar.text).replace('\t', '').replace('\n', '')
            jeden_zart.append(zarr)

    try:
        x = jeden_zart[random.randrange(0, 20, 1)]
    except IndexError:
        try:
            x = jeden_zart[random.randrange(0, 1, 1)]
        except IndexError:
            x = 'Brak pozycji do przeczytania'

    return x


def kategorie_wykonanie():
    x = pobranie_strony('policjant')
    kategory = zarty_kategorie(x)

    return str(kategory)
