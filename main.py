import requests
import array
from bs4 import BeautifulSoup
import json 



# def repeat():
# 	tab=1
# 	while(tab<5):
# 		print(tab)
# 		tab=tab+1

# repeat()



mainurl='https://www.1mg.com/'



def getComposition(url):
	response = requests.get(url)
	html = response.content
	soup = BeautifulSoup(html,'lxml')
	for drug in soup.find_all(class_="DrugInfo__drug-name-heading___adCs-"):
		print 'Drugname '+ (drug.text)
	for company in soup.find_all(class_="DrugInfo__company-name___39Abk"):
		print 'Company '+ (company.text)
	for composition in soup.find_all(class_="saltInfo DrugInfo__salt-name___2-9Vh"):
		print 'Composition '+ composition.a.text




def getData(url):
	response=requests.get(url)
	html=response.content
	soup=BeautifulSoup(html,'lxml')
	for a in soup.find_all(class_="link-brand"):
		getComposition(mainurl+a.get('href'))
	


def allTabdata():
	tab=1
	while (tab<56):
		dataurl="https://www.1mg.com/drugs-listaz?api=true&pageNumber="+str(tab)+"&name=B&_=1529314636770"
		print dataurl
		resp = requests.get(url=dataurl)
		data = resp.json()
		result = data['result']
		for item in result:
			url=item.get('url')
			getData(mainurl+url)
		tab=tab+1		
	

# allTabdata(dataurl,tab)
allTabdata()



# resp = requests.get(url=dataurl)
# data = resp.json()
# result=data['result']
# print result

# for item in result:
# 	url=item.get('url')
# 	print mainurl+url
# 	getData(mainurl+url)
	



















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

