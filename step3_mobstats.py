from bs4 import BeautifulSoup
from urllib.parse import urljoin
from datetime import datetime
import requests
import csv

base = 'https://wiki.project1999.com/'
npclinks = 'step2b_cleanup.txt'

def cyclelinks(filename):
    global urList
    # include .txt when passing in filename
    fileopen = open(filename).readlines()
    urList = [listitem.rstrip() for listitem in fileopen]
    # print(urList)

cyclelinks(npclinks)

maxurlnum = len(urList)
print(maxurlnum)

uindex = 0
def getstats():
    global uindex
    while uindex <= maxurlnum:
        scrapeurl = urList[uindex]
        #index of a list, in a file.
        req = requests.get(scrapeurl)
        soup = BeautifulSoup(req.content, 'html.parser')

        # # Get Wiki Entry Title [of the mob...] && print it
        wikititle = soup.title.string.replace(' - Project 1999 Wiki', '')
        print(wikititle)

        happtable = soup.find("table", attrs={"class": "mobStatsBox"})
        happtable_data = happtable.findAll("tr")
        # open a CSV file with append, so old data will not be erased
        with open('step3.csv', 'a') as mobstats:
            for mobStats in happtable_data:
                res = mobStats.find('td')                                             
                if res:
                    global mobInfo
                    mobInfo = res.text.strip()
                    #print(mobInfo)
                    csvstats = csv.writer(mobstats)
                    csvstats.writerow([wikititle, mobInfo, scrapeurl])

        if uindex == maxurlnum:
            break
        elif maxurlnum + 1 == True:
            break
        else:
            uindex += 1


    #print(uindex)
    getstats()
        
getstats()