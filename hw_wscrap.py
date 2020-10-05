import requests
from bs4 import BeautifulSoup


# определяем список ключевых слов
KEYWORDS = ['дизайн', 'web', 'python']
set_keywords = set(KEYWORDS)

response = requests.get('https://habr.com/ru/all/')
soup = BeautifulSoup(response.text, 'html.parser')
el_all = soup.find_all(class_="content-list__item content-list__item_post shortcuts_item")

new_list = []
for el in el_all:

    set_hub = el.find(
       class_='post post_preview'
    )

    set_hub = (str(set_hub).lower())

    for word in KEYWORDS:
        if word in set_hub:
            hubs_date = el.find(class_="post__time").text
            hubs_link = el.find(class_='post__title_link')['href']
            hubs_text = el.find(class_="post__title_link").text
            new_list.append(f'<{hubs_date}> - <{hubs_text}> - <{hubs_link}>')

print(set(new_list))


