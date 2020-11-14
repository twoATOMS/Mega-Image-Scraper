# Library
import datetime
from scipy.stats.mstats import gmean # pentru medie
from urllib.request import urlopen
from bs4 import BeautifulSoup # scraping library

PRODUSE = {
    'faina':'https://www.mega-image.ro/Ingrediente-culinare/Zahar-faina-si-malai/Faina/c/007001004?q=%3Arelevance',
    'malai':'https://www.mega-image.ro/Ingrediente-culinare/Zahar-faina-si-malai/Malai/c/007001006?q=%3Arelevance',
    'paine':'https://www.mega-image.ro/Cafea-cereale-si-mic-dejun/Paine-si-specialitati/Paine/c/005004001?q=%3Arelevance',
    'franzelarie':'https://www.mega-image.ro/Cafea-cereale-si-mic-dejun/Paine-si-specialitati/Altele/c/005004004?q=%3Arelevance',
    'cozonac':'https://www.mega-image.ro/Cafea-cereale-si-mic-dejun/Paine-si-specialitati/Cozonac-si-chec/c/005004003?q=%3Arelevance',
    'cartofi':'https://www.mega-image.ro/Fructe-si-legume-proaspete/Legume-proaspete/Cartofi/c/001003002',
    'fasole':'https://www.mega-image.ro/Fructe-si-legume-proaspete/Legume-proaspete/Fasole-verde-uscata/c/001003008?q=%3Arelevance',
    'legume':'https://www.mega-image.ro/Fructe-si-legume-proaspete/Legume-proaspete/c/001003?q=%3Arelevance&sort=relevance&pageNumber=0',
    'fructe':'https://www.mega-image.ro/Fructe-si-legume-proaspete/Fructe-proaspete/c/001001',
    'citrice':'https://www.mega-image.ro/Fructe-si-legume-proaspete/Fructe-proaspete/Citrice/c/001001008?q=%3Arelevance&pageNumber=0',
    'ulei':'https://www.mega-image.ro/Ingrediente-culinare/Ulei-otet-si-suc-de-lamaie/Ulei-de-floarea-soarelui/c/007003002?pageNumber=0',
    'margarina':'https://www.mega-image.ro/Lactate-si-oua/Unt-si-margarina/Margarina/c/002004002?pageNumber=0',
    'carne de pasare':'https://www.mega-image.ro/Mezeluri-carne-si-ready-meal/Carne-proaspata/Carne-de-pasare/c/003002002?q=%3Arelevance',
    'carne de vita':'https://www.mega-image.ro/Mezeluri-carne-si-ready-meal/Carne-proaspata/Carne-de-vita/c/003002003?q=%3Arelevance',
    'carne de porc':'https://www.mega-image.ro/Mezeluri-carne-si-ready-meal/Carne-proaspata/Carne-de-porc/c/003002001?q=%3Arelevance',
    'preparate din carte':'https://www.mega-image.ro/Mezeluri-carne-si-ready-meal/Carne-proaspata/Carne-tocata-mici-si-altele/c/003002004?q=%3Arelevance&pageNumber=0',
    'peste':'https://www.mega-image.ro/Produse-congelate/Carne-peste-si-fructe-de-mare-congelate/Peste/c/004002002',
    'lapte':'https://www.mega-image.ro/Lactate-si-oua/Lapte/Lapte-de-consum-integral/c/002001003?q=%3Arelevance&pageNumber=0',
    'telemea de vaca':'https://www.mega-image.ro/Lactate-si-oua/Branzeturi/Telemea-vaca/c/002002009?q=%3Arelevance&pageNumber=0',
    'telemea de oaie':'https://www.mega-image.ro/Lactate-si-oua/Branzeturi/Telemea-oaie/c/002002008?q=%3Arelevance',
    'unt':'https://www.mega-image.ro/Lactate-si-oua/Unt-si-margarina/Unt/c/002004001?q=%3Arelevance',
    'oua':'https://www.mega-image.ro/Lactate-si-oua/Oua/Pachet-10-oua/c/002005002',
    'zahar':'https://www.mega-image.ro/Ingrediente-culinare/Zahar-faina-si-malai/Zahar-alb/c/007001009',
    'miere':'https://www.mega-image.ro/Cafea-cereale-si-mic-dejun/Dulceata-miere-si-creme-tartinabile/Miere/c/005006004',
    'cafea':'https://www.mega-image.ro/Cafea-cereale-si-mic-dejun/Cafea/Cafea-macinata/c/005001006?pageNumber=0',
    'vin':'https://www.mega-image.ro/Bauturi-si-tutun/Vinuri/Vin-alb/c/009002001?q=%3Arelevance',
    'bere':'https://www.mega-image.ro/Bauturi-si-tutun/Bere-si-Cidru/Bere-blonda/c/009001001?q=%3Arelevance&pageNumber=0',
    
    }

# Scrape algo
preturi = list()

for fiecare_produs in PRODUSE.keys():
    index0 = 0
    try:
        while index0 < 20:
            html = urlopen(PRODUSE[fiecare_produs])
            bsObj = BeautifulSoup(html.read(), 'html.parser')
            
            pret = bsObj.find_all('span', {'class':'quantity-price super-bold'})[index0].get_text()
            preturi.append(float(pret.split()[0].replace(',','.')))
            
            index0 += 1
    except IndexError:
        print("S-a terminat lista de preturi la",fiecare_produs,'!',"Total:",index0)
        
print()
print()
print()
print("Media Geometrica este:",round(gmean(preturi),4),',','data:',datetime.date.today())