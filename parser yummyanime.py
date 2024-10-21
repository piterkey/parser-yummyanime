##! /usr/bin/env python
## -*- coding: utf-8 -*-
import urllib.request
from urllib.request import Request
from bs4 import BeautifulSoup

animesite = 'https://yummyanime.tv/user/'


def get_html(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urllib.request.urlopen(req).read()
    return webpage


def main():
    id_ = input("Write your profile name on site {0}".format(animesite).strip()) or "admin"
    soup = BeautifulSoup(get_html(animesite + id_), "html.parser")

    my_yammyanime = {'watching': 'tabz-1', 'watched': 'tabz-2', 'planned': 'tabz-3', 'postponed': 'tabz-4',
                     'abandoned': 'tabz-5', 'favorites': 'tabz--1'}

    with open("{0}_animelist.txt".format(id_), 'w', newline='', encoding="utf-8") as animefile:
        for key, value in my_yammyanime.items():
            animefile.write('\n' + '-----' + key + '-----' + '\n')
            tabz_list = soup.find_all(name='div', id=value)
            anime_list = tabz_list[0].find_all(name='a', attrs="popular-item__title ws-nowrap")
            for anime in anime_list:
                # print(anime.text, anime['href'])
                animefile.write('- ' + anime.text + '; ' + anime['href'] + '\n')
    print("Your anime lists written to {0}_animelist.txt".format(id_))


if __name__ == '__main__':
    main()
