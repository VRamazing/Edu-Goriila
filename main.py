__author__ = "vignesh ramesh"

import requests
from bs4 import BeautifulSoup

res = requests.get("http://www.thelearningpoint.net/system/app/pages/search?scope=search-site&q=school&offset=0")
res.raise_for_status()
content =res.content #get html content
soup = BeautifulSoup(content,'html.parser')
outputFile = open('output.txt', 'w')


for s in soup.findAll("div",{"class":"sites-search-result"}):
	link=s.find("a").get('href')
	getData = requests.get("http://www.thelearningpoint.net/" + link).content
	# getData.raise_for_status()
	dataSoup = BeautifulSoup(getData,'html.parser')
	tableSoup = dataSoup.find("table",{"class":"sites-layout-name-one-column sites-layout-hbox"}).find('table')
	print(tableSoup)
	name = tableSoup.contents[3].find("td",{"height":"8", "width":"494"}).string.strip()
	email = tableSoup.contents[13].find("td",{"height":"8", "width":"494"}).string.strip()
	output = name + "," + email
	outputFile.write(output + '\n')
	
	

