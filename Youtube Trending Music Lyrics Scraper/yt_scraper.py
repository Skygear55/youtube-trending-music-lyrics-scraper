# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 21:47:36 2020

@author: k.kirilov
"""
from support import title_truncator
from support import scrape_song_lyrics
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")


url = 'https://www.youtube.com/feed/trending?bp=4gIuCggvbS8wNHJsZhIiUExGZ3F1TG5MNTlhbkJodVBsX3k3d1k1MGtiMGh5WW16bw%3D%3D' 

DRIVER_PATH = "C:/Users/k.kirilov/Downloads/chromedriver_win32/chromedriver.exe"

driver = webdriver.Chrome(options = options, executable_path = DRIVER_PATH)

driver.get("https://www.youtube.com/feed/trending?bp=4gIuCggvbS8wNHJsZhIiUExGZ3F1TG5MNTlhbkJodVBsX3k3d1k1MGtiMGh5WW16bw%3D%3D")



titles = driver.find_elements_by_id("video-title")
text_titles = []

for title in titles: 
    text_titles.append(title.text)
  
#original_titles = text_titles.copy()    

for i in range(len(text_titles)): 
    text_titles[i] = title_truncator(text_titles[i])
    
driver.close()
lyrics = {}


for title in text_titles:
    url = "https://genius.com/" + title + "lyrics"
    print(url)
    i = 0
    while(i < 10):
        try:
            lyrics[title] = scrape_song_lyrics(url)
            #lyrics.append(scrape_song_lyrics(url))
        except AttributeError:
            print("retrying...")
            i += 1
        else:
            break
    
print(lyrics)
