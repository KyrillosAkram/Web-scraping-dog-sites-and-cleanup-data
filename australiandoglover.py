from json import loads
from urllib.request import urlopen
from bs4 import BeautifulSoup, NavigableString,re
from ssl import SSLContext
import requests

USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
headerRow  =['NAME','APPEARANCE','TEMPERAMENT','HEALTH','HOUSEPET POTENTIAL','SPACE & EXERCISE','ACTIVITIES AND DOG SPORTS','GROOMING','RECOMMENDED FOR']
textoftitles=[]
#existed_spans=[]
def scrape_breed_links():
	mycontext=SSLContext()
	urlLink="https://www.australiandoglover.com/p/know-your-breed.html"
	response=requests.get(urlLink,headers=USER_AGENT)#urlopen(urlLink,context=mycontext,headers=USER_AGENT)
	bsobj=BeautifulSoup(response.text,"lxml")
	Breed=[]
	Breed=bsobj.html.body.findAll('div',{'class':'separator'})
	for i in range(len(Breed)):
		Breed[i]=Breed[i].a['href']
	return Breed

def between(cur, end):
	if cur=='None':
		return 'None'
	while cur and cur != end:
		if isinstance(cur, NavigableString):
			text = cur.strip()
			if len(text):
				yield text
		cur = cur.next_element

def find_title_position(title,no_of_titles,existed_spans):
	'''
	to detect where the title placed
	'''
	at=-1
	for j in range(no_of_titles):
		if (re.match('%s'%(title),existed_spans[j].get_text())):#.replace('\n','').replace(' - Breed Profile','')
			at=j
			break
	return at


def scrape_all_breeds(breed_links):
	breeds_info=[]
	mycontext=SSLContext()
	x=0
	starlist=[]
	for breed in breed_links:
		print('[%0.3i]\tscraping %s'%(x,breed))
		response=requests.get(breed,headers=USER_AGENT)
		bsobj=BeautifulSoup(response.text,'lxml')
		name=bsobj.find('h3',{'class':'post-title entry-title'}).get_text().replace('\n','').replace(' - Breed Profile','')
		existed_spans=bsobj.findAll('span',{'style':re.compile(r'(color: orange;)|(color: #8e7cc3;)|(color: #3d85c6;)|(color: red; font-family: Verdana, sans-serif;)|(color: #674ea7; font-family: "georgia" , "times new roman" , serif; font-size: large;)')})
		#print(existed_spans)
		#textoftitles=[]
		no_spans=len(existed_spans)
		#print(labda: tag for tag in existed_spans)
		#print('no_spans is %d'%(no_spans))
		for i in range(no_spans):
			if (i < (no_spans-1)):
				textoftitles.append(' '.join(text for text in between(existed_spans[i].findNext(),existed_spans[i].findNext('span',{'style':re.compile(r'(color: orange;)|(color: #8e7cc3;)|(color: #3d85c6;)')}))))
			else :
				try :
					textoftitles.append(' '.join(text for text in between(existed_spans[i].findNext(),existed_spans[i].findNext())))
				except :
					textoftitles.append('can\'t scrape')

		title_position={
			'APPEARANCE':find_title_position('APPEARANCE',no_spans,existed_spans),
			'TEMPERAMENT':find_title_position('TEMPERAMENT',no_spans,existed_spans),
			'HEALTH':find_title_position('HEALTH',no_spans,existed_spans),
			'HOUSEPET POTENTIAL':find_title_position('HOUSEPET POTENTIAL',no_spans,existed_spans),
			'SPACE & EXERCISE':find_title_position('SPACE & EXERCISE',no_spans,existed_spans),
			'ACTIVITIES AND DOG SPORTS':find_title_position('ACTIVITIES AND DOG SPORTS',no_spans,existed_spans),
			'GROOMING':find_title_position('GROOMING',no_spans,existed_spans),
			'RECOMMENDED FOR':find_title_position('RECOMMENDED FOR',no_spans,existed_spans)
		}

		breed_info={
			'NAME'						:name,
			'APPEARANCE'				:textoftitles[title_position['APPEARANCE']] if title_position['APPEARANCE']!=-1 else 'not available',
			'TEMPERAMENT'				:textoftitles[title_position['TEMPERAMENT']] if title_position['TEMPERAMENT']!=-1 else 'not available',
			'HEALTH'					:textoftitles[title_position['HEALTH']] if title_position['HEALTH']!=-1 else 'not available',
			'HOUSEPET POTENTIAL'		:textoftitles[title_position['HOUSEPET POTENTIAL']] if title_position['HOUSEPET POTENTIAL']!=-1 else 'not available',
			'SPACE & EXERCISE'			:textoftitles[title_position['SPACE & EXERCISE']] if title_position['SPACE & EXERCISE']!=-1 else 'not available',
			'ACTIVITIES AND DOG SPORTS'	:textoftitles[title_position['ACTIVITIES AND DOG SPORTS']] if title_position['ACTIVITIES AND DOG SPORTS']!=-1 else 'not available',
			'GROOMING'					:textoftitles[title_position['GROOMING']] if title_position['GROOMING']!=-1 else 'not available',
			'RECOMMENDED FOR'			:textoftitles[title_position['RECOMMENDED FOR']] if title_position['RECOMMENDED FOR']!=-1 else 'not available'
			}
		breeds_info.append(breed_info)
		x=x+1
		del breed_info ,title_position
		textoftitles.clear()
	return breeds_info

'''
'NAME','HISTORY','APPEARANCE','TEMPERAMENT','HEALTH','HOUSEPET POTENTIAL','SPACE & EXERCISE','ACTIVITIES AND DOG SPORTS','GROOMING','RECOMMENDED FOR'
'''
'''		HEALTH_tag=bsobj.find('span',{'style':re.compile(r'(color: orange;)|(color: #8e7cc3;)|(color: #3d85c6;)')},text=re.compile('HEALTH') )
		HOUSEPETPOTENTIAL_tag=bsobj.find('span',{'style':re.compile(r'(color: orange;)|(color: #8e7cc3;)|(color: #3d85c6;)')},text=re.compile('HOUSEPET POTENTIAL') )
		SPACEEXERCISE_tag=bsobj.find('span',{'style':re.compile(r'(color: orange;)|(color: #8e7cc3;)|(color: #3d85c6;)')},text=re.compile('SPACE & EXERCISE') )
		ACTIVITIESANDDOGSPORTS_tag=bsobj.find('span',{'style':re.compile(r'(color: orange;)|(color: #8e7cc3;)|(color: #3d85c6;)')},text=re.compile('SPACE & EXERCISE') )
'''
		