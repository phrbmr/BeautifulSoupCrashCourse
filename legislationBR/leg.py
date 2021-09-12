import os
import time
#os.system('pip install --upgrade pip')
#os.system('pip install beautifulsoup4')
#os.system('pip install lxml')
#os.system('pip install requests[security]')
#os.system('pip install pandas')

## WebScraping tools
from bs4 import BeautifulSoup
import requests

#Data Analisys Tools
import pandas as pd
import numpy as np

# Scrape Legislation
def leg():
  url = 'https://www.in.gov.br/en/web/dou/-/lei-n-14.181-de-1-de-julho-de-2021-329476499'

  html_text = requests.get(url).text
  soup = BeautifulSoup(html_text, 'html.parser')

  lei = soup.find(class_='identifica')
  ementa = soup.find(class_='ementa')
  links = soup.find_all('a', class_='dou-paragraph')

  #print(f'{lei.text}\n- {ementa.text}')
  #print(links)


  for link in soup.find_all('a'):
    print(link.get('href'))


if __name__ == "__main__":
  leg()