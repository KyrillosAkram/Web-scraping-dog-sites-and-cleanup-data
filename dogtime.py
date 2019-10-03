from json import loads
from urllib.request import urlopen
from bs4 import BeautifulSoup, NavigableString,re
from ssl import SSLContext
import requests

USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
headerRow  =['Name','stars Adaptability','stars Adapts Well to Apartment Living','stars Good For Novice Owners','stars Sensitivity Level','stars Tolerates Being Alone','stars Tolerates Cold Weather','stars Tolerates Hot Weather','stars All Around Friendliness','stars Affectionate with Family','stars Incredibly Kid Friendly Dogs','stars Dog Friendly','stars Friendly Toward Strangers','stars Health Grooming','stars Amount Of Shedding','stars Drooling Potential','stars Easy To Groom','stars General Health','stars Potential For Weight Gain','stars Size','stars Trainability','stars Easy To Train','stars Intelligence','stars Potential For Mouthiness','stars Prey Drive','stars Tendency To Bark Or Howl','stars Wanderlust Potential','stars Energy Level','stars Intensity','stars Exercise Needs','stars Potential For Playfulness','Dog Breed Group','Height','Weight','Life Span','Highlights','size','Personality','Health','Care','Feeding','Coat Color And Grooming','Children And Other Pets','Rescue Groups','Breed Organizations']
def scrape_breed_links():
	mycontext=SSLContext()
	urlLink="https://dogtime.com/dog-breeds/profiles/"
	response=requests.get(urlLink,headers=USER_AGENT)#urlopen(urlLink,context=mycontext,headers=USER_AGENT)
	bsobj=BeautifulSoup(response.text,"lxml")
	Breed=[]
	Breed=bsobj.html.body.findAll('a',{'class':'list-item-title'})
	return Breed
	#print('%0.3i breed link found and scraped successfull ...'%len(Breed))

def getstar(tag):
	x=1
	while (x<6):
		numstar='star-{}'.format(x)
		if(tag==numstar):
			break
		x=x+1
	return x

			

def scrape_all_breeds(breed_links):
	breeds_info=[]
	mycontext=SSLContext()
	x=0
	starlist=[]
	for breed in breed_links:
		print('[%0.3i]\tscraping %s'%(x,breed_links[x]['href']))
		response=requests.get(breed_links[x]['href'],headers=USER_AGENT)
		bsobj=BeautifulSoup(response.text,'lxml')
		ratelist=bsobj.html.body.findAll('div',{'class':re.compile('^star')})
		starlist.clear()
		if len(ratelist)==30:
			for i in range(30):
				starlist.append(getstar(ratelist[i]['class'][1]))
			if(breed_links[x]['href']=='https://dogtime.com/dog-breeds/doxiepoo'):
				starlist.insert(14,'not available')
			if(breed_links[x]['href']=='https://dogtime.com/dog-breeds/jindo'):
				starlist.insert(24,'not available')
					
			
		else:
			for i in range(31):
				starlist.append(getstar(ratelist[i]['class'][1]))
			
		vital=bsobj.findAll('div',{'class':'vital-stat-box'})
		org=bsobj.find('h3',{'class':'js-section-heading description-title'},text='Breed Organizations')
		rg=bsobj.find('h3',{'class':'js-section-heading description-title'},text='Rescue Groups')
		children=bsobj.find('h3',{'class':'js-section-heading description-title'},text='Children And Other Pets')
		cc=bsobj.find('h3',{'class':'js-section-heading description-title'},text='Coat Color And Grooming')
		Feeding=bsobj.find('h3',{'class':'js-section-heading description-title'},text='Feeding')
		care=bsobj.find('h3',{'class':'js-section-heading description-title'},text='Care')
		health=bsobj.find('h3',{'class':'js-section-heading description-title'},text='Health')
		Personality=bsobj.find('h3',{'class':'js-section-heading description-title'},text='Personality')
		sizee=bsobj.find('h3',{'class':'js-section-heading description-title'},text='Size')
		Highlights=bsobj.find('h3',{'class':'js-section-heading description-title'},text='Highlights')
		
		
		breed_info={
			'Name'										:breed_links[x].get_text(),
			'stars Adaptability'						:starlist[0],
			'stars Adapts Well to Apartment Living'		:starlist[1],
			'stars Good For Novice Owners'				:starlist[2],
			'stars Sensitivity Level'					:starlist[3],
			'stars Tolerates Being Alone'				:starlist[4],
			'stars Tolerates Cold Weather'				:starlist[5],
			'stars Tolerates Hot Weather'				:starlist[6],
			'stars All Around Friendliness'				:starlist[7],
			'stars Affectionate with Family'			:starlist[8],
			'stars Incredibly Kid Friendly Dogs'		:starlist[9],
			'stars Dog Friendly'						:starlist[10],
			'stars Friendly Toward Strangers'			:starlist[11],
			'stars Health Grooming'						:starlist[12],
			'stars Amount Of Shedding'					:starlist[13],
			'stars Drooling Potential'					:starlist[14],
			'stars Easy To Groom'						:starlist[15],
			'stars General Health'						:starlist[16],
			'stars Potential For Weight Gain'			:starlist[17],
			'stars Size'								:starlist[18],
			'stars Trainability'						:starlist[19],
			'stars Easy To Train'						:starlist[20],
			'stars Intelligence'						:starlist[21],
			'stars Potential For Mouthiness'			:starlist[22],
			'stars Prey Drive'							:starlist[23],
			'stars Tendency To Bark Or Howl'			:starlist[24],
			'stars Wanderlust Potential'				:starlist[25],
			#stars 'Exercise Needs'						:starlist[26],
			'stars Energy Level'						:starlist[27],
			'stars Intensity'							:starlist[28],
			'stars Exercise Needs'						:starlist[29],
			'stars Potential For Playfulness'			:starlist[30],
			'Dog Breed Group'							:vital[0].get_text()[16:],
			'Height'									:vital[1].get_text()[7:],
			'Weight'									:vital[2].get_text()[7:],
			'Life Span'									:vital[3].get_text()[10:],
			'Highlights'								:Highlights.findNext().get_text() if Highlights else 'not available',
			'size'										:sizee.findNext().get_text() if sizee else 'not available',
			'Personality'								:Personality.findNext().get_text()if Personality else 'not available',
			'Health'									:health.findNext().get_text() if health else 'not available',
			'Care'										:care.findNext().get_text() if care else 'not available',
			'Feeding'									:Feeding.findNext().get_text() if Feeding else 'not available',
			'Coat Color And Grooming'					:cc.findNext().get_text() if cc else 'not available',
			'Children And Other Pets'					:children.findNext().get_text() if children else 'not available',
			'Rescue Groups'								:rg.findNext().get_text() if rg else 'not available',
			'Breed Organizations'						:org.findNext().get_text() if org else 'not available'
			}
		breeds_info.append(breed_info)
		x=x+1
	return breeds_info
