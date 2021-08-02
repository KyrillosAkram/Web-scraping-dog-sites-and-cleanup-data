from json import loads
from urllib.request import urlopen
from bs4 import BeautifulSoup, NavigableString,re
from ssl import SSLContext

headerRow=['Name','size','Breed History','Character','Temperament','Conformation','Colour','Training','Care','Health','Kennel Club Group','My ideal owner(s)','What they say about me']

def scrape_root_json():
	mycontext=SSLContext()
	urlLink="http://www.noahsdogs.com/m/dogs/ajaxselection?sortby=alphabetical&page=0&perpage=1000&imagetype=undefined"
	response=urlopen(urlLink,context=mycontext)
	bsobj=BeautifulSoup(response,"lxml")
	Breed=bsobj.html.body.get_text()
	Breed=loads(Breed.replace("\\'", "'"))
	return Breed

def xtract_breed_links(jsn):
	print('%i breed founded !'%(int(jsn['totals'])))
	breed_links=[]
	for link in range(int(jsn['totals'])):
		breed_links.append(jsn[str(link)]['uri'])
	return breed_links

def between(cur, end):
	if cur=='None':
		return 'None'
	while cur and cur != end:
		if isinstance(cur, NavigableString):
			text = cur.strip()
			if len(text):
				yield text
		cur = cur.next_element

def scrape_all_breeds(breed_links,root_jsn):
	breeds_info=[]
	mycontext=SSLContext()
	x=0
	for breed in breed_links:
		print('[%0.3i]\tscraping %s'%(x,"http://www.noahsdogs.com"+breed))
		response=urlopen("http://www.noahsdogs.com"+breed,context=mycontext)
		bsobj=BeautifulSoup(response,'lxml')
		try:
			size=' '.join(text for text in between(bsobj.find('p', text='Size:').next_sibling,bsobj.find('h3', text='Popularity:')))
			Kennel_Club_Group=' '.join(text for text in between(bsobj.find('p', text='Kennel Club Group:').next_sibling,bsobj.find('p', text='Size:'))),

		except:
			size='not available'
			try:
				Kennel_Club_Group=' '.join(text for text in between(bsobj.find('p', text='Kennel Club Group:').next_sibling,bsobj.find('h3', text='Popularity:'))),
			except:
				Kennel_Club_Group='not available'
		
		
		breed_info={
			'Name'					:root_jsn[str(x)]['petname'],
			'size'					:size,
			'Breed History' 		:' '.join(text for text in between(bsobj.find('h3', text='Breed History:').next_sibling,bsobj.find('h3', text='Character:'))),
			'Character'				:' '.join(text for text in between(bsobj.find('h3', text='Character:').next_sibling,bsobj.find('h3', text='Temperament:'))),
			'Temperament'			:' '.join(text for text in between(bsobj.find('h3', text='Temperament:').next_sibling,bsobj.find('h3', text='Conformation:'))),
			'Conformation'			:' '.join(text for text in between(bsobj.find('h3', text='Conformation:').next_sibling,bsobj.find('h3', text='Colour:'))),
			'Colour'				:' '.join(text for text in between(bsobj.find('h3', text='Colour:').next_sibling,bsobj.find('h3', text='Training:'))),
			'Training'				:' '.join(text for text in between(bsobj.find('h3', text='Training:').next_sibling,bsobj.find('h3', text='Care:'))),
			'Care'					:' '.join(text for text in between(bsobj.find('h3', text='Care:').next_sibling,bsobj.find('h3', text='Health:'))),
			'Health'				:' '.join(text for text in between(bsobj.find('h3', text='Health:').next_sibling,bsobj.find('p', text='You may also like:'))),
			'Kennel Club Group' 	:Kennel_Club_Group,
			'My ideal owner(s)'		:' '.join(text for text in between(bsobj.find('h3', text='My ideal owner(s)').next_sibling,bsobj.find('h3', text='What they say about me'))),
			'What they say about me':' '.join(text for text in between(bsobj.find('h3', text='What they say about me').next_sibling,bsobj.find('p', text=re.compile('Please read on'))))
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
