from bs4 import BeautifulSoup

with open("index.html", 'r') as f:
	soup_string = BeautifulSoup(f.read(), 'html.parser')
	print(soup_string)
