import requests
from bs4 import BeautifulSoup

url="https://www.kariyer.net/is-ilanlari"
get=requests.get(url)
#print(get.status_code) --> 200 response geldi, basarili. user agenta gerek yok. 
content=get.content
soup=BeautifulSoup(content,"lxml")
titles=soup.find_all("div", {"class": "k-space d-flex xLarge right"})
for i in titles:
    i=i.text
    print(i)


