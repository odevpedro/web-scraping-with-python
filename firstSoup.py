import requests
from bs4 import BeautifulSoup


#Web scrapping using a local html file
'''
with open("index.html", 'r') as f:
	soup_string = BeautifulSoup(f.read(), 'html.parser')
	print(soup_string)
'''

#now using a external link
'''
r = requests.get('http://www.google.com')
soup = BeautifulSoup(r.text, 'lxml')
print(soup)
'''

#using html5lib
'''
with open('index.html', 'r') as f: 
	soup_string = BeautifulSoup(f.read(), 'html5lib')
print(soup_string)
'''

#acess a specific tag in html file
'''
with open('index.html', 'r') as f: 
	soup = BeautifulSoup(f, 'lxml')

tag = soup.title # that is valid for any tag that is put after
print(tag)
'''



#getting into a tag
with open('index.html', 'r') as f: 
	soup = BeautifulSoup(f, 'lxml')

tag = soup.p.get_text()
print(tag)