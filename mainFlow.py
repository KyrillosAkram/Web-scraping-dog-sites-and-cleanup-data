from time import time
import csv

scrape_noah                 = True if input("Do you want to scrape noahsdogs.com ?\t\t\t(y/n) :\n\t")=='y'else False
scrape_dogtime              = True if input("Do you want to scrape dogtime.com ?\t\t\t(y/n) :\n\t")=='y'else False
scrape_australiandoglover   = True if input("Do you want to scrape australiandoglover.com ?\t\t(y/n) :\n\t")=='y'else False
scrape_selectadogbreed		= True if input("Do you want to scrape selectadogbreed.com ?\t\t(y/n) :\n\t")=='y'else False

start=time()

if(scrape_noah):
	print('loading to scrape noah ...')
	import noah
	print('scraping root json ...')
	breeds_json=noah.scrape_root_json()
	print('extracting breeds links ...')
	breed_links=noah.xtract_breed_links(breeds_json)
	breeds_info=noah.scrape_all_breeds(breed_links,breeds_json)

	print('writing to noah.csv')
	noah_csv_path='./noahsdogs.csv'
	deskaccess=open(noah_csv_path,'w')
	writing_manager=csv.writer(deskaccess)
	writing_manager.writerow(noah.headerRow)
	for i in range(int(breeds_json['totals'])):#,breeds_info
		try:
			writing_manager.writerow([breeds_info[i]['Name'],breeds_info[i]['size'],breeds_info[i]['Breed History'],breeds_info[i]['Character'],breeds_info[i]['Temperament'],breeds_info[i]['Conformation'],breeds_info[i]['Colour'],breeds_info[i]['Training'],breeds_info[i]['Care'],breeds_info[i]['Health'],breeds_info[i]['Kennel Club Group'],breeds_info[i]['My ideal owner(s)'],breeds_info[i]['What they say about me']])
			pass
		except:
			continue
	deskaccess.close()

if(scrape_dogtime):
	print('loading to scrape dogtime ...')
	import dogtime
	print('scraping breed links ...')
	breed_links=dogtime.scrape_breed_links()
	number_of_breeds=len(breed_links)
	print('%0.3i breed link found ...'%(number_of_breeds))
	print('scraping breeds from links ...')
	#breed_links=dogtime.xtract_breed_links(breeds_json)
	breeds_info=dogtime.scrape_all_breeds(breed_links)
	print('writing to dogtime.csv')
	dogtime_csv_path='./dogtime.csv'
	deskaccess=open(dogtime_csv_path,'w')
	writing_manager=csv.writer(deskaccess)
	writing_manager.writerow(dogtime.headerRow)
	for i in range(number_of_breeds):#,breeds_info
		try:
			writing_manager.writerow([breeds_info[i]['Name'],breeds_info[i]['stars Adaptability'],breeds_info[i]['stars Adapts Well to Apartment Living'],breeds_info[i]['stars Good For Novice Owners'],breeds_info[i]['stars Sensitivity Level'],breeds_info[i]['stars Tolerates Being Alone'],breeds_info[i]['stars Tolerates Cold Weather'],breeds_info[i]['stars Tolerates Hot Weather'],breeds_info[i]['stars All Around Friendliness'],breeds_info[i]['stars Affectionate with Family'],breeds_info[i]['stars Incredibly Kid Friendly Dogs'],breeds_info[i]['stars Dog Friendly'],breeds_info[i]['stars Friendly Toward Strangers'],breeds_info[i]['stars Health Grooming'],breeds_info[i]['stars Amount Of Shedding'],breeds_info[i]['stars Drooling Potential'],breeds_info[i]['stars Easy To Groom'],breeds_info[i]['stars General Health'],breeds_info[i]['stars Potential For Weight Gain'],breeds_info[i]['stars Size'],breeds_info[i]['stars Trainability'],breeds_info[i]['stars Easy To Train'],breeds_info[i]['stars Intelligence'],breeds_info[i]['stars Potential For Mouthiness'],breeds_info[i]['stars Prey Drive'],breeds_info[i]['stars Tendency To Bark Or Howl'],breeds_info[i]['stars Wanderlust Potential'],breeds_info[i]['stars Energy Level'],breeds_info[i]['stars Intensity'],breeds_info[i]['stars Exercise Needs'],breeds_info[i]['stars Potential For Playfulness'],breeds_info[i]['Dog Breed Group'],breeds_info[i]['Height'],breeds_info[i]['Weight'],breeds_info[i]['Life Span'],breeds_info[i]['Highlights'],breeds_info[i]['size'],breeds_info[i]['Personality'],breeds_info[i]['Health'],breeds_info[i]['Care'],breeds_info[i]['Feeding'],breeds_info[i]['Coat Color And Grooming'],breeds_info[i]['Children And Other Pets'],breeds_info[i]['Rescue Groups'],breeds_info[i]['Breed Organizations']])
			pass
		except:
			continue
	deskaccess.close()


if(scrape_australiandoglover):
	print('loading to scrape australiandoglover ...')
	import australiandoglover
	print('scraping breed links ...')
	breed_links=australiandoglover.scrape_breed_links()
	breed_links.remove('http://www.australiandoglover.com/2015/10/the-pug.html')   # as this page is completly empty 
	#print(breed_links)
	number_of_breeds=len(breed_links)
	print('%0.3i breed link found ...'%(number_of_breeds))
	print('scraping breeds from links ...')
	#breed_links=dogtime.xtract_breed_links(breeds_json)
	breeds_info=australiandoglover.scrape_all_breeds(breed_links)
	print('writing to australiandoglover.csv')
	australiandoglover_csv_path='./australiandoglover.csv'
	deskaccess=open(australiandoglover_csv_path,'w')
	writing_manager=csv.writer(deskaccess)
	writing_manager.writerow(australiandoglover.headerRow)
	for i in range(number_of_breeds):#,breeds_info
		try:
			writing_manager.writerow([breeds_info[i]['NAME'],breeds_info[i]['APPEARANCE'],breeds_info[i]['TEMPERAMENT'],breeds_info[i]['HEALTH'],breeds_info[i]['HOUSEPET POTENTIAL'],breeds_info[i]['SPACE & EXERCISE'],breeds_info[i]['ACTIVITIES AND DOG SPORTS'],breeds_info[i]['GROOMING'],breeds_info[i]['RECOMMENDED FOR']])
			pass
		except:
			continue
	deskaccess.close()

if(scrape_selectadogbreed):
	print('loading to scrape selectadogbreed ...')
	import selectadogbreed
	print('scraping breeds tag ...')
	breeds_tag=selectadogbreed.scrape_breeds_tag()
	no_breeds=len(breeds_tag)
	print('%0.3i breed link found ...'%(no_breeds))
	print('extracting breeds index ...')
	breeds_index=selectadogbreed.xtract_breeds_index(breeds_tag)
	breeds_info=selectadogbreed.scrape_all_breeds(breeds_index)

	print('writing to selectadogbreed.csv')
	selectadogbreed_csv_path='./selectadogbreed.csv'
	deskaccess=open(selectadogbreed_csv_path,'w')
	writing_manager=csv.writer(deskaccess)
	writing_manager.writerow(selectadogbreed.headerRow)
	for i in range(no_breeds):#,breeds_info
		try:
			writing_manager.writerow([breeds_info[i]['Name'],breeds_info[i]['Category'],breeds_info[i]['Weight'],breeds_info[i]['HealthRisk'],breeds_info[i]['LifeExpectancy'],breeds_info[i]['Coat'],breeds_info[i]['GroomingIntensity'],breeds_info[i]['MonthlyCost'],breeds_info[i]['Trainability'],breeds_info[i]['ActivityLevel'],breeds_info[i]['Purpose'],breeds_info[i]['Content'],breeds_info[i]['AdditionalContent']])
			pass
		except:
			continue
	deskaccess.close()



end=time()
print('\n\n\aCrawling finished after %f s from staring'%(end-start))
#print(breeds_info[0]['What they say about me'])