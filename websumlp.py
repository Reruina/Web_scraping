import urllib.request
import bs4
import re

url = 'http://granbluefantasy.jp/news/'

soup = bs4.BeautifulSoup(urllib.request.urlopen(url).read(),'lxml')

#print(soup)

response = urllib.request.urlopen(url)

data = response.read()

#dat = re.sub("本文を読む＞ ","",data)

#print(data)

for a in soup.find_all('a','change_news_trigger'):
    #print(a)
    print(a.string)