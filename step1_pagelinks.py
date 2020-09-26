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

#moblinks = []
#def getmoblink():
#    moblinks.append(urljoin(base, relative))
#    if 'mw-pages' not in relative:
#        getmoblink()
#        print(relative)
#        
#    lml = len(moblinks)
#    
#    if lml > 0:
#        print(lml)
        

#def regnpc_nonmw(): # or just add an else code above
#    for link in connie:
#        if link['href']:
#            relative = link['href']
#            links.append(urljoin(base, relative))
##
#def uncle():
#    
#        with open('npclinks.txt', 'a') as scrapelinks:
#            scrapelinks.write(str(mwpage))
#            print(str(mwpage))
#    unclenewurl()



# run uncle function here,
# use first url
# will take next url
# and scrape that

# ONCE THIS PASSES WE NEED TO REINITIALIZE URL AS A NEW VALUE
# RUN THE SCRAPER AGAIN FOR A NEW #MW-PAGE LINK
# THEN REPEAT

#
### function to get unique values 
#def unique(passlist):
#    global uni
#    # intilize a null list 
#    uni = []
#
#    # traverse for all elements 
#    for x in passlist: 
#        # check if exists in unique_list or not 
#        if x not in uni: 
#            uni.append(x)
#            url = uni[-1]
#            print('new url passed', url)
#            return url
#
#



#mw = soup.find("div", {"id": "mw-pages"})
#connie = mw.findAll('a')
#
#links = []
#for link in connie:
#    if link.has_attr('href'):
#        relative = link['href']
#        links.append(urljoin(base, relative))
#
#
#with open('npclinks.txt', 'a') as scrapelinks:
#    scrapelinks.write(str(links))
#    print(' ')
#    print(str(links))
#    



#from bs4 import BeautifulSoup
#import requests
#from datetime import datetime
#from urllib.parse import urljoin
#
#base = 'https://wiki.project1999.com/'
#url = "https://wiki.project1999.com/index.php?title=Category:NPCs#mw-pages"
#        
#        
#        
#        
#        
#r = requests.get(url)
#soup = BeautifulSoup(r.text, 'html.parser')
#
#mw = soup.find("div", {"id": "mw-pages"})
#connie = mw.findAll('a')
#
#links = []
#for link in connie:
#    if link.has_attr('href'):
#        relative = link['href']
#        links.append(urljoin(base, relative))
#
#
#with open('npclinks.txt', 'a') as scrapelinks:
#    scrapelinks.write(str(links))
#    print(' ')
#    print(str(links))