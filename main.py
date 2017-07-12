__author__ = "vignesh ramesh"

import requests
from bs4 import BeautifulSoup

outputFile = open('output.txt', 'w')
i=0
while(i<=10):

	res = requests.get("http://www.thelearningpoint.net/system/app/pages/search?scope=search-site&q=school&offset=" + str(i))
	print(res.raise_for_status())
	print('request' + str(i))
	content =res.content #get html content
	soup = BeautifulSoup(content,'html.parser')

	for s in soup.findAll("div",{"class":"sites-search-result"}):
		link=s.find("a").get('href')
		getData = requests.get("http://www.thelearningpoint.net/" + link).content
		# getData.raise_for_status()c
		dataSoup = BeautifulSoup(getData,'html.parser')
		tableSoup = dataSoup.find("table",{"class":"sites-layout-name-one-column sites-layout-hbox"}).find('table',{"border":"1","cellspacing":"1","width":"96%"})

		if tableSoup  != None:
			name = tableSoup.contents[3].find('td',{'valign':'top'}).b.string
			if name == 'Name of Institution':
				name = tableSoup.contents[3].td.next_sibling.string
				email = tableSoup.contents[13].td.next_sibling.string
			else:
				name = ''
				email = ''

		else:
			name =dataSoup.find('span',{'id':'sites-page-title','dir':'ltr','tabindex':'-1'}).string.split(":")[0]
			email = ''

	

		print(name.strip() + ',' + email.strip() )
		output = name.strip() + "," + email.strip()
		outputFile.write(output + '\n')

	i+=1







	
	
	

