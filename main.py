import requests
import array
from bs4 import BeautifulSoup
import json 


def getData(url):
	response=requests.get(url)
	html=response.content
	soup=BeautifulSoup(html,'lxml')
	for my_tag in soup.find_all(class_="button-text text-small text-blue link-brand"):
		print(my_tag.text)



mainurl='https://www.1mg.com/'
dataurl='https://www.1mg.com/drugs-listaz?api=true&pageNumber=1&name=B&_=1529314636770'
resp = requests.get(url=dataurl)
data = resp.json()
result=data['result']
# print result

for item in result:
	url=item.get('url')
	print mainurl+url
	getData(mainurl+url)
	# response=requests.get('https://www.1mg.com//brands/t-bact-dC1iYWN0')
	# html=response.content
	# soup=BeautifulSoup('html','lxml')
	# for tag in soup.find_all(class_="button-text text-small text-blue link-brand"):
	# 	print (my_tag.text)


# url = 'https://www.1mg.com/brands/betadine-YmV0YWRpbmU='
# response = requests.get(url)
# html = response.content
# soup = BeautifulSoup(html,'lxml')
# for my_tag in soup.find_all(class_="button-text text-small text-blue link-brand"):
#     print(my_tag.text)


















# for link in soup.findAll('a'):
#     print(link.get('href'))
# print soup.prettify()

