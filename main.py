__author__ = "vignesh ramesh"

import requests
from bs4 import BeautifulSoup

res = requests.get("http://www.thelearningpoint.net/system/app/pages/search?scope=search-site&q=school&offset=0")
res.raise_for_status()
content =res.content #get html content
soup = BeautifulSoup(content,'html.parser')
element =soup.findAll("div",{"class":"sites-search-result"})

print(element)