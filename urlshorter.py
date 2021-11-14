import urllib.request
url = 'https://www.youtube.com/watch?v=E6o_luoNGDU'
fetcher = urllib.request.urlopen(
  'https://clck.ru/--?url=' +
  url)
print(fetcher.read())
# 'https://clck.ru/8JM'
