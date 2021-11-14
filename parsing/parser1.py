import requests
from bs4 import BeautifulSoup

originalfilename = 'orig'
translatedfilename = 'trans'
url = 'https://www.amalgama-lab.com/songs/d/disturbed/who_taught_you_how_to_hate.html'
r = requests.get(url)
soup = BeautifulSoup(r.text)
origlang = soup.find_all('div', {'class': 'original' })
with open('{}.txt'.format(originalfilename), 'w') as outfile:
    for line in origlang:
        outfile.write(line.text)
translated = soup.find_all('div', {'class': 'translate' })
with open('{}.txt'.format(translatedfilename), 'w') as outfile:
    for line in translated:
        outfile.write(line.text)

