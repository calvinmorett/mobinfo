![npclinks](/img/npclinks.png "npclinks")

Mobinfo is just mob information for p99, webscrapped from the project1999 wiki.

Steps:
Use beautifulsoup to siphon all [next_page] links
Use those pulled links to scrape each page for more links, each which contain about 200 links to NPC pages
A quick clean up of those links is done with step2b
Then those NPC pages are cycled through with bs4, and the mob information is then pulled and all information is saved to a CSV

Libraries used:
- beautifulsoup
- urllib
- requests
- csv
- datetime

![inprogress web scrape](/img/mobinfo.gif "Web Scraping each link")
