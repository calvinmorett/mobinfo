from bs4 import BeautifulSoup
import requests
from datetime import datetime
from urllib.parse import urljoin

base = 'https://wiki.project1999.com/'
url = "https://wiki.project1999.com/index.php?title=Category:NPCs&pageuntil=A+Contemplative+Thifling#mw-pages"

breakloop = False
mwpage = []
        
def soupy(scrape_url):
    global relative
    r = requests.get(scrape_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    mw = soup.find("div", {"id": "mw-pages"})
    connie = mw.findAll('a', href=True)
    
    for link in connie:
        if link['href']:
            relative = link['href']
            
def pl(scrape_url):
    global breakloop
    soupy(scrape_url)
    
    if 'pagefrom' in relative and breakloop == False:
        mwpage.append(urljoin(base, relative))
        next_page = mwpage[-1]
        # print(next_page)
        # print(len(mwpage))
        with open('step1.txt', 'a+') as pagelinks:
            pagelinks.write(str(next_page)+'\n')
        if 'pagefrom=Zordakalicus' in relative:
            pagelinks.write(str(next_page)+'\n')
            print('Zor hit, ending function loop')
            breakloop = True
            #print(mwpage)
        else:
            pl(next_page)
        
pl(url)
