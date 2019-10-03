from time import time
import csv
start=time()

scrape_noah=False
scrape_dogtime=True
if(scrape_noah):
    print('loading to scrape noah ...')
    import noah
    print('scraping root json ...')
    breeds_json=noah.scrape_root_json()
    print('extracting breeds links ...')
    breed_links=noah.xtract_breed_links(breeds_json)
    breeds_info=noah.scrape_all_breeds(breed_links,breeds_json)

    print('writing to noah.csv')
    noah_csv_path='/mnt/369071E49071AB4F/MyLab/Space/project_box/new/noahsdogs.csv'
    deskaccess=open(noah_csv_path,'w')
    writing_manager=csv.writer(deskaccess)
    writing_manager.writerow(noah.headerRow)
    for i in range(int(breeds_json['totals'])):#,breeds_info
        writing_manager.writerow([breeds_info[i]['Name'],breeds_info[i]['size'],breeds_info[i]['Breed History'],breeds_info[i]['Character'],breeds_info[i]['Temperament'],breeds_info[i]['Conformation'],breeds_info[i]['Colour'],breeds_info[i]['Training'],breeds_info[i]['Care'],breeds_info[i]['Health'],breeds_info[i]['Kennel Club Group'],breeds_info[i]['My ideal owner(s)'],breeds_info[i]['What they say about me']])
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
    dogtime_csv_path='/mnt/369071E49071AB4F/MyLab/Space/project_box/new/dogtime.csv'
    deskaccess=open(dogtime_csv_path,'w')
    writing_manager=csv.writer(deskaccess)
    writing_manager.writerow(dogtime.headerRow)
    for i in range(number_of_breeds):#,breeds_info
        writing_manager.writerow([breeds_info[i]['Name'],breeds_info[i]['stars Adaptability'],breeds_info[i]['stars Adapts Well to Apartment Living'],breeds_info[i]['stars Good For Novice Owners'],breeds_info[i]['stars Sensitivity Level'],breeds_info[i]['stars Tolerates Being Alone'],breeds_info[i]['stars Tolerates Cold Weather'],breeds_info[i]['stars Tolerates Hot Weather'],breeds_info[i]['stars All Around Friendliness'],breeds_info[i]['stars Affectionate with Family'],breeds_info[i]['stars Incredibly Kid Friendly Dogs'],breeds_info[i]['stars Dog Friendly'],breeds_info[i]['stars Friendly Toward Strangers'],breeds_info[i]['stars Health Grooming'],breeds_info[i]['stars Amount Of Shedding'],breeds_info[i]['stars Drooling Potential'],breeds_info[i]['stars Easy To Groom'],breeds_info[i]['stars General Health'],breeds_info[i]['stars Potential For Weight Gain'],breeds_info[i]['stars Size'],breeds_info[i]['stars Trainability'],breeds_info[i]['stars Easy To Train'],breeds_info[i]['stars Intelligence'],breeds_info[i]['stars Potential For Mouthiness'],breeds_info[i]['stars Prey Drive'],breeds_info[i]['stars Tendency To Bark Or Howl'],breeds_info[i]['stars Wanderlust Potential'],breeds_info[i]['stars Energy Level'],breeds_info[i]['stars Intensity'],breeds_info[i]['stars Exercise Needs'],breeds_info[i]['stars Potential For Playfulness'],breeds_info[i]['Dog Breed Group'],breeds_info[i]['Height'],breeds_info[i]['Weight'],breeds_info[i]['Life Span'],breeds_info[i]['Highlights'],breeds_info[i]['size'],breeds_info[i]['Personality'],breeds_info[i]['Health'],breeds_info[i]['Care'],breeds_info[i]['Feeding'],breeds_info[i]['Coat Color And Grooming'],breeds_info[i]['Children And Other Pets'],breeds_info[i]['Rescue Groups'],breeds_info[i]['Breed Organizations']])
    deskaccess.close()




end=time()
print('\n\n\aCrawling finished after %f s from staring'%(end-start))
#print(breeds_info[0]['What they say about me'])