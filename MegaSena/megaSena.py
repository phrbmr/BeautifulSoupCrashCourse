import os
#os.system('pip install --upgrade pip')
#os.system('pip install beautifulsoup4')
#os.system('pip install lxml')
#os.system('pip install requests')
#os.system('pip install pandas')

from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests
import time

url = 'http://loterias.caixa.gov.br/wps/portal/loterias/landing/megasena/!ut/p/a1/04_Sj9CPykssy0xPLMnMz0vMAfGjzOLNDH0MPAzcDbwMPI0sDBxNXAOMwrzCjA0sjIEKIoEKnN0dPUzMfQwMDEwsjAw8XZw8XMwtfQ0MPM2I02-AAzgaENIfrh-FqsQ9wNnUwNHfxcnSwBgIDUyhCvA5EawAjxsKckMjDDI9FQE-F4ca/dl5/d5/L2dBISEvZ0FBIS9nQSEh/pw/Z7_HGK818G0K8DBC0QPVN93KQ10G1/res/id=historicoHTML/c=cacheLevelPage/=/'

def megaSena():
  
  html_text = requests.get(url).text
  soup = BeautifulSoup(html_text, 'lxml')

  table = soup.find_all('table')
  table_headings = soup.find_all('th') #list of headings
  table_data = soup.tbody.find_all('tr') #list rows

  #extracting and cleaning the headings
  headings = []
  for h in table_headings:
    headings.append(h.text.strip())
  
  # extracting and cleaning the data
  body = []
  for row in table_data:
    subrow = soup.tbody.find_all('td')
    
    for sr in subrow:
      body.append(sr.text)
    #clean = row.text.strip()
    #clean = clean.replace(" ", "")
    #item = clean.split('\n')

    #if item != ['']:
    #  body.append(item)
  
  print(body)
  df = pd.DataFrame(columns=headings)
  


  
  

if __name__ == '__main__':
  megaSena()