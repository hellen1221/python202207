# web1.py
from bs4 import BeautifulSoup 

page = open("test01.html", "rt", encoding="utf-8").read()


soup = BeautifulSoup(page, "html.parser")
#print(soup.prettify())
#<p>태그전체를 검색
#print(soup.find_all("p"))
#<a>태그전체를 검색
#print(soup.find_all("a"))
#find()는 1개를 검색
#print(soup.find("p")) #1개
#필터링 : <p class='outer-text'>인경우
#파이썬 키워드로 class와 충동방지를 위해 class_
#print(soup.find_all("p", class_='outer-text'))

for tag in soup.find_all("p"):
    print(tag.txt)