# class="b-post  b-post_padbot_15 b-post_margbot_20 b-post_bordbot_eee b-post_relative "
import requests
from bs4 import BeautifulSoup
import time

pages = 5

for page in range(1, pages):
    url = 'https://www.fl.ru/projects/?page={}&kind=5'.format(page)
    r = requests.get(url)
    time.sleep(2)
    soup = BeautifulSoup(r.text)

    titles = soup.find_all('h2', {'class': 'b-post__title b-post__title_inline'})
    with open('fl_tasks.txt', 'a') as outfile:
        for line in titles:
            outfile.write(line.text.rstrip())
