#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 

Course work: 

@author:

Source:
    https://en.wikipedia.org/wiki/Petta_(film)
'''
import requests
from bs4 import BeautifulSoup


def get_actors(item):

    return None

def start():
    
    #print('Main')
    
    # Collect and parse first page
    page = requests.get('https://en.wikipedia.org/wiki/Petta_(film)')
    soup = BeautifulSoup(page.text, 'html.parser')    
    
    #print(soup)    

    items = soup.select('table.infobox tr')

    '''
        Movie:
        Movie Name
        Release Date
        Lead Actor(s)
        Lead Actress(es)
        Support Actors
        Music Director
        Director
    '''
    movie_dict = {
        'movie_name' : None,
        'release_date' : None,
        'lead_actors' : None,
        'lead_actresses' : None,
        'support_actors' : None,
        'music_director' : None,
        'director' : None
    }

    item_list = ''
    for item in items:
        c_th = item.find("th")

        # print(type(c_th))

        if(not c_th):
            continue 

        c_td = item.find("td")  

        if(not c_td):
            continue

        key = c_th.get_text()

        if(key == 'Directed by'):
            val = c_td.get_text()

            movie_dict['director'] = val
        elif(key == 'Music by'):
            val = c_td.get_text()

            movie_dict['music_director'] = val


    print(movie_dict)

if __name__ == '__main__':
    start()        