import os
#os.system('pip install --upgrade pip')
#os.system('pip install beautifulsoup4')
#os.system('pip install lxml')
#os.system('pip install requests')

from bs4 import BeautifulSoup
import requests
import time

def find_jobs():
  html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
  
  soup = BeautifulSoup(html_text, 'lxml')
  jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

  for index, job in enumerate(jobs):
    publish_date = job.find('span', class_='sim-posted').span.text.strip()
  
    if 'few' in publish_date:
      skills = job.find('span', class_='srp-skills').text.strip() #get abd clean skills
      skills = skills.replace(' ', '')
    
      if off_skill not in skills:
        company_name = job.find('h3', class_='joblist-comp-name').text #only text
        company_name = company_name.strip() # remove white space and line break
        more_info = job.header.h2.a['href']
        with open(f'posts/{index}.txt', 'w') as f:      
          f.write(f'''
          ____________________________
          Company name: {company_name}
          Required Skills: {skills}
          More Info: {more_info}
          Publish Date: {publish_date}
          ____________________________
          ''')
        print(f'File saved: {index}.txt')

off_skill = input('Filter out skills\n >')
print(f'Filtering out {off_skill}')

if __name__ == '__main__':
  while True:
    find_jobs()
    wait_time = 1
    print(f'\nWaiting {wait_time} minutes\n')
    time.sleep(wait_time * 60)