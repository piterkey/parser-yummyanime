##! /usr/bin/env python
## -*- coding: utf-8 -*-
import csv
import urllib.request
from urllib.request import Request
from bs4 import BeautifulSoup


def get_html(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urllib.request.urlopen(req).read()
    return webpage

def parse(html):
    soup = BeautifulSoup(html, "html.parser")
    watched = soup.find('div', class_ = 'content-page top-page')
    projects_names = []
    projects_views = []
    projects_ratings = []
    projects_votes = []
    data = []
    # if watched != None:
    for name in watched.find_all('a', class_ = 'anime-title'):
        projects_names.append({
            name.text
        })
    for view in watched.find_all('div', class_ = 'preview-info-block custom-scroll'):
        f_view = view.p.text.split()
        temp = ' '.join(map(str, f_view[1:]))
        projects_views.append({
            temp 
        })

    for div0 in watched.find_all('span', class_ = 'main-rating-block'):
        cols = div0.find_all('span')
        projects_ratings.append({
            cols[0].text
        })
    for div1 in watched.find_all('span', class_ = 'main-rating-block'):
        cols = div1.find_all('span')
        f_div1 = str(cols[1].text).strip('()')
        temp = f_div1.split()
        n_temp = temp[0]
        print(n_temp)
        # temp = f_div1[6]
        projects_votes.append({
            n_temp
        })
    i, name, view, rate, vote = 0, 0, 0, 0, 0
    while i == 0:
        try:
            data.append ( [projects_names[name], projects_views[view], projects_ratings[rate], projects_votes[vote]])
            name +=1
            view +=1
            rate+=1
            vote+=1
        except: break
    return data

def save (data, path):
    with open(path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(('Название', 'Просмотров','Рейтинг' ,'Голосов'))
        for line in data:
            cell = dict({'Название':line[0], 'Просмотров':line[1],'Рейтинг':line[2] ,'Голосов':line[3]})
            print(line)
            print(cell)
            writer.writerow((', '.join(cell['Название']), ', '.join(cell['Просмотров'])  ,  ', '.join(cell['Рейтинг']),  ', '.join(cell['Голосов'] ) ))

def main():
    data = []
    data.extend(parse(get_html('https://yummyanime.club/top')))
    save(data, 'top100.csv')
fetch#test
#test2

if __name__ == '__main__':
    main()
