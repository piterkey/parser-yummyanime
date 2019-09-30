##! /usr/bin/env python
## -*- coding: utf-8 -*-
import csv
import urllib.request
from urllib.request import Request
from bs4 import BeautifulSoup

num = 0
def get_html(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urllib.request.urlopen(req).read()
    return webpage

def parse(html):
    soup = BeautifulSoup(html, "html.parser")
    alist = ['watch_now', 'will', 'watched', 'lost', 'favourite']
    watched = soup.find('div', id = alist[get_value()])
    projects = []
    if watched != None:
        for lis in watched.find_all('li'):
            cols = lis.find_all('span')
            try: projects.append({
                'Название': cols[0].span.text.strip(),
                'Рейтинг':  cols[0].find(class_= 'user-rating').text.strip()
            })
            except:
                projects.append({ 'Название': cols[0].span.text.strip() })
        return projects
def save (projects, path):
    with open(path, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(('Название', 'Рейтинг'))

        for project in projects:
            try: 
                writer.writerow((project['Название'], project['Рейтинг']))
            except: 
                writer.writerow((project['Название'],))

def main():
    id_ = input('Write your id(yummyanime.club/users/id...):')
    alist = ['anime watching1.csv', 'anime will1.csv', 'anime watched1.csv', 'anime lost1.csv', 'anime favourite1.csv']
    for tag in alist:
        projects = []
        try:
            projects.extend(parse(get_html('https://yummyanime.club/users/id'+ id_)))
            save(projects, tag)
            set_value(get_value()+1)
        except: 
            continue
def get_value():
    global num
    return num 

def set_value(new_value):
    global num
    num = new_value

if __name__ == '__main__':
    main()
