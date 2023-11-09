from bs4 import BeautifulSoup
import requests

url = 'https://zinduaschool.com/blog/'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
content = soup.find('div', class_='content-wrap')
articles = content.findAll('article')

for article in articles:
    title = article.find('h2', class_='entry-title').text



print(title)
