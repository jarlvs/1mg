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


download_dir = "B1mg.csv" 
csv = open(download_dir, "w") 
columnTitleRow = "Drugname, Companyname, Composition\n"
csv.write(columnTitleRow)



mainurl='https://www.1mg.com/'


# get all data we want from unique drug
def getComposition(url):
	response = requests.get(url)
	html = response.content
	soup = BeautifulSoup(html,'lxml')

	for drug in soup.find_all(class_="DrugInfo__drug-name-heading___adCs-"):
		Drugname = drug.text
		if(len(Drugname)>0):
			print 'Drugname ' + Drugname
		else:
			Drugname = " "


	for company in soup.find_all(class_="DrugInfo__company-name___39Abk"):
		Companyname = company.text
		if(len(Companyname)>0):
			print 'Companyname ' + Companyname
		else:
			Companyname = " "


	for composition in soup.find_all(class_="saltInfo"):
		Composition = composition.a.text
		if(len(Composition)>0):
			print 'Composition '+composition.a.text
		else:
			Composition = " ";




	row = Drugname + ", " + Companyname + ", " + Composition + "\n"
	csv.write(row)






def getData(url):
	response=requests.get(url)
	html=response.content
	soup=BeautifulSoup(html,'lxml')
	for a in soup.find_all(class_="link-brand"):
		getComposition(mainurl+a.get('href'))
	

# get urls of all urls which will open corresponding number of drugs of particular drug  

def allTabdata():
	tab=2
	while (tab<59):
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

