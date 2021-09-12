##################################################################
# An exercise working with:
#   1. Beautiful Soup:   to web scrape
#   2. Pandas:           to convert to a DataFrame
#   3. Pygsheets:        to automatcaly export to google sheets
#   4. Replit secret enviroment
##################################################################

import os
import time
#os.system('pip install --upgrade pip')
#os.system('pip install beautifulsoup4')
#os.system('pip install lxml')
#os.system('pip install requests[security]')
#os.system('pip install pandas')
#os.system('pip install pygsheets')



## WebScraping tools
from bs4 import BeautifulSoup
import requests

#Data Analisys Tools
import pandas as pd
import numpy as np

# Getting the countries and flags from the web
def flag():
  url = 'https://www.worldometers.info/geography/flags-of-the-world/'

  #beatifoulsoup routines to get the data from website
  html_text = requests.get(url).text
  soup = BeautifulSoup(html_text, 'lxml')
  flags = soup.find_all('div', class_='col-md-4')

  #cleaning file and initializing counter
  open('flags.txt', 'w').close()
  i = 0

  #getting flag name & link and exporting to a file
  for flag in flags:
    i +=1
    try:
      with open('flags.txt','a') as f: 
        f.write(f"{flag.text}_: https://www.worldometers.info{flag.find('a')['href']}\n")
    except TypeError:
      print(f'Type Error at line {flag.text}')
      break
  
  #converting file to a DataFrame
  df = pd.read_csv('flags.txt', engine='python', sep="_:")
  df.columns = ['Country',	'Link']
  print(df)

  #authorization to r and w on google sheets
  #import pygsheets
  #paises = '1S_Sj-iRGKo9A7P_WeT2bxrE5dOij3_Q9E9p3v6cKFa0' #key of the sheet
  #client = pygsheets.authorize(custom_credentials = 'API_KEY')
  #client.open_by_key(paises)
  
  


if __name__ == "__main__":
  flag()