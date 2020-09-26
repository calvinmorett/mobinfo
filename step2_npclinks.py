from bs4 import BeautifulSoup
from urllib.parse import urljoin
from datetime import datetime
import requests

base = 'https://wiki.project1999.com/'
pagelinks = 'step1.txt'

def cyclelinks(filename):
    global urList
    # include .txt when passing in filename
    fileopen = open(filename).readlines()
    urList = [listitem.rstrip() for listitem in fileopen]
    #urList = [listitem for listitem in fileopen]
    #print(urList)

cyclelinks(pagelinks)

maxurlnum = len(urList)
print(maxurlnum)

uindex = 0
def getlinks():
    global uindex
    while uindex <= maxurlnum:
        scrape_url = urList[uindex]
        #index of a list, in a file.
        r = requests.get(scrape_url)
        soup = BeautifulSoup(r.text, 'html.parser')

        mw = soup.find("div", {"id": "mw-pages"})
        connie = mw.findAll('a')

        with open('step2.txt', 'a+') as npclinks:
            for link in connie:
                if link.has_attr('href'):
                    relative = link['href']
                    based_npc = urljoin(base, relative)
                    npclinks.write(str(based_npc)+'\n')

        if uindex == maxurlnum:
            break
        elif maxurlnum + 1 == True:
            break
        else:
            uindex += 1
    getlinks()
    
getlinks()