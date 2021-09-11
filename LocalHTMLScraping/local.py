import os
#os.system('pip install --upgrade pip')
#os.system('pip install beautifulsoup4')
#os.system('#pip install lxml')

from bs4 import BeautifulSoup

# reading the file
with open('home.html', 'r') as html_file:
  content = html_file.read()
  
  # creating the soup object
  soup = BeautifulSoup(content, 'lxml')
  
  ## Getting a list of tags 
  #courses_html_tags = soup.find_all('h5')
  #for course in courses_html_tags:
  #  print(course.text)

  ##getting course cards and prices
  course_cards = soup.find_all('div', class_= 'card' ) #underscore in 'class_'
  for course in course_cards:
    course_name = course.h5.text
    course_price = course.a.text.split()[-1]

    print(f'{course_name} costs {course_price}')
    




