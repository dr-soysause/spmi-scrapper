import time
import requests
from bs4 import BeautifulSoup
import json


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}

persons_page_url = []

for i in range(0, 21):
    url = f'http://personalii.spmi.ru/ru/glossary?page={i}'
    response = requests.get(url=url, headers=headers)
    result = response.content
    soup = BeautifulSoup(result, 'lxml')
    persons = soup.find_all(class_='info small-12 medium-8 large-9 columns')

    for person in persons:
        person_page_url ='http://personalii.spmi.ru' + person.find('a')['href']
        persons_page_url.append(person_page_url)

progress = len(persons_page_url)

with open('persons_urls.txt', 'a') as file:
    for line in persons_page_url:
        file.write(f'{line}\n')

with open('persons_urls.txt') as file:

    lines = [line.strip() for line in file.readlines()]

    data_dict = []

    count = 0
    
    for line in lines:
        q = requests.get(line)
        result = q.content
        soup = BeautifulSoup(result, 'lxml')
        full_name = soup.find('h1').text.strip()
        degree = soup.find(class_='small-12 medium-6 large-7 columns').find('span', text='Должность').next_sibling.strip()
        try:
            department = soup.find(class_='small-12 medium-6 large-7 columns').find('a').text.strip()
        except AttributeError:
            department = 'none'
        tel = soup.find_all('div', {'class':'small-12 medium-6 large-6 columns'})[1].text.strip()
        
        data = {
            'full_name': full_name,
            'degree': degree,
            'department': department,
            'tel': tel
        }

        count += 1
        print(f'{count}:{line} --{round((count/progress*100), 2)}% DONE--')

        data_dict.append(data)

        with open(file='data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data_dict, json_file, ensure_ascii=False, indent=4)

        time.sleep(2)

print('\nComplited!')


