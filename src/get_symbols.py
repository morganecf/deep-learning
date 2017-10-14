import urllib.request
from bs4 import BeautifulSoup

url = 'http://symboldictionary.net/library/graphics/symbols/'

with urllib.request.urlopen(url) as response:
  html = response.read()

soup = BeautifulSoup(html)
links = [url + img.get('href') for img in soup.find_all('a')]

# aa.jpg is the first symbol, there's junk before that
index = links.index('http://symboldictionary.net/library/graphics/symbols/aa.jpg')
links = links[index:]

# save urls
print('Saving', len(links), 'urls')
with open('symbol_urls.txt', 'w') as fp:
  for link in links:
    fp.write(link + '\n')

# save images
for link in links:
  name = link.split('/')[-1]
  print('Downloading', name)
  with open('sigils/' + name, 'wb') as fp:
    with urllib.request.urlopen(link) as response:
      image = response.read()
    fp.write(image)

