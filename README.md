![](https://github.com/calvinmorett/img/blob/main/skull_crop.gif)

Mobinfo is just mob information for Everquest, webscrapped from the project1999 wiki.

1. Use beautifulsoup to siphon all [next 200] links
2. Use those pulled links to scrape each page for more links, each which contain about 200 links to NPC pages
3. A quick clean up of those links is done with step2b
4. Then those NPC pages are cycled through with bs4, and the mob information is then pulled and all information is saved to a CSV

![inprogress web scrape](/img/mobinfo.gif "Web Scraping each link")

Libraries used:
- beautifulsoup
- urllib
- requests
- csv
- datetime
- re

![npclinks](/img/npclinks.png "npclinks")
