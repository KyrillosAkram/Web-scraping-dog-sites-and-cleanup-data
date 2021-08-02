from json import loads
from urllib.request import urlopen
from bs4 import BeautifulSoup, NavigableString,re
from ssl import SSLContext

headerRow=['Name','Category','Weight','HealthRisk','LifeExpectancy','Coat','GroomingIntensity','MonthlyCost','Trainability','ActivityLevel','Purpose','Content','AdditionalContent']

def scrape_breeds_tag():
	mycontext=SSLContext()
	urlLink="https://www.selectadogbreed.com/search-for-dog-breeds/"
	response=urlopen(urlLink,context=mycontext)
	bsobj=BeautifulSoup(response,"lxml")
	Breed=bsobj.findAll('a',{'class':'breed-read-more-search'})
	#Breed=loads(Breed.replace("\\'", "'"))
	return Breed[1:]

def xtract_breeds_index(jsn):
	#print('%i breed founded !'%(len(jsn)))
	breeds_index=[]
	for link in jsn:
		breeds_index.append((link['ng-click'][9:-1]).replace(')',''))
	#breeds_index=breeds_index.remove('r.Id')
	return breeds_index

def between(cur, end):
	if cur=='None':
		return 'None'
	while cur and cur != end:
		if isinstance(cur, NavigableString):
			text = cur.strip()
			if len(text):
				yield text
		cur = cur.next_element

def get_all_category(categorylist):
	categorytext=''
	for category in categorylist:
		categorytext=categorytext+category['CategoryName']+' '
	return categorytext

def scrape_all_breeds(breeds_index):
	breeds_info=[]
	mycontext=SSLContext()
	x=0
	for breed in breeds_index:
		print('[%0.3i]\tscraping %s'%(x,"https://www.selectadogbreed.com/umbraco/surface/breeddetail/index/?q="+breed))
		response=urlopen("https://www.selectadogbreed.com/umbraco/surface/breeddetail/index/?q="+breed,context=mycontext)
		bsobj=BeautifulSoup(response.read().decode('utf-8'),'lxml')
		dicit=bsobj.html.body.get_text().replace('\\u0026','&').replace('\\r\\n','    ').replace('\\u003cp\\u003e','').replace('\\u003c/p\\u003e','').replace('\\u003cstrong\\u003e','').replace('\\u003c/strong\\u003e','').replace('\\u003cbr /\\u003e','').replace('\xa0','').replace("\\'", "'")
		Breed=loads(dicit)[0]

		breed_info={
			'Name'				:Breed['Name'],
			'Category'			:get_all_category(Breed['Category']),
			'Weight'		 	:Breed['Weight'],
			'HealthRisk'		:Breed['HealthRisk'],
			'LifeExpectancy'	:Breed['LifeExpectancy'],
			'Coat'				:Breed['Coat'],
			'GroomingIntensity'	:Breed['GroomingIntensity'],
			'MonthlyCost'		:Breed['MonthlyCost'],
			'Trainability'		:Breed['Trainability'],
			'ActivityLevel'		:Breed['ActivityLevel'],
			'Purpose'			:Breed['Purpose'],
			'Content'			:Breed['Content'],
			'AdditionalContent'	:Breed['AdditionalContent']
			}
		breeds_info.append(breed_info)
		x=x+1
	return breeds_info

'''
'Name','size','Breed History','Character','Temperament','Conformation','Colour','Training','Care','Health','Kennel Club Group','My ideal owner(s)','What they say about me'
'''
	
'''
' '.join(text for text in between(bsobj.find('h3', text='Character:').next_sibling,bsobj.find('h3', text='Temperament:')))
'''

'''
['Name','Category','Weight','HealthRisk','LifeExpectancy','Coat','GroomingIntensity','MonthlyCost','Trainability','ActivityLevel','Purpose','Content','AdditionalContent']
'''