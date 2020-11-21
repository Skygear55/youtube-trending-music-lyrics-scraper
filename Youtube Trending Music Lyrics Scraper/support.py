# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 22:36:26 2020

@author: k.kirilov
"""
from bs4 import BeautifulSoup
import requests
""" Function truncates and formats the titles so that they can be directly input to search for genius url"""
def title_truncator(title):  #argument must be a string
    permissible_letters = " '-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"  
    
    for i in range(len(title)-2): 
        if title[i] not in permissible_letters: 
           title = title.replace(title[i:len(title)], "")
           break
       
        title = title.replace('-', ' ')
        title = title.replace('  ', ' ')
        title = title.replace(' x ', ' ')
        title = title.replace(' ', '-')
        title = title.replace("'", "")
        if title[-1] != "-": 
            title = title + "-"
        

       

    return title

def scrape_song_lyrics(url):
    page = requests.get(url)
    html = BeautifulSoup(page.text, 'html.parser')
    lyrics = html.find('div', class_='lyrics').get_text()        
    return lyrics

