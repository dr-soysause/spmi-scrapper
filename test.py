from unicodedata import name
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}

# person_list= []

# url = 'http://personalii.spmi.ru/ru/glossary?page=0'
# response = requests.get(url=url, headers=headers)
# result = response.content

# soup = BeautifulSoup(result, 'lxml')
# persons = soup.find_all(class_='info small-12 medium-8 large-9 columns')
# for person in persons:
#     person_page_url ='http://personalii.spmi.ru' + person.find('a')['href']
#     # last_name = person.find('h2').get_text()
#     # second_name = person.find('h3').get_text()
#     # full_name = last_name + ' ' + second_name
#     # second_name = person.get('h3')
#     print(person_page_url)
#     # for i, j in persons:
#     #     full_name = ([i+j])
#     #     person_list.append(full_name)

response = requests.get(url='http://personalii.spmi.ru/ru/glossary/a/abiev_zaur_agaddovich')
result = response.content
soup = BeautifulSoup(result, 'lxml')
full_name = soup.find('h1').text.strip()
degree = soup.find(class_='small-12 medium-6 large-7 columns').find('span', text='Должность').next_sibling.strip()
department = soup.find(class_='small-12 medium-6 large-7 columns').find('a').text
tel = soup.find_all('div', {'class':'small-12 medium-6 large-6 columns'})[1].text.strip()
print(department)
