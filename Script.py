import requests
import bs4
from datetime import date, timedelta as td

def getnews(url):
    def no_class(tag):
        return tag.has_attr('href') and not tag.has_attr('class')
    newsraw=requests.get(url).text
    start=newsraw.find('<section class="content">')
    end=newsraw.find('<div class="y-d">')
    news=newsraw[start:end]
    newsbs=bs4.BeautifulSoup(news)
    newslist=newsbs.find_all(no_class)
    return newslist

def dates():
    d1 = date(2016,1,1) #you can change the starting date if needed
    d2 = date(2016,10,18) ##you can change the end date if needed
    diff = d2 - d1
    datelist=[]
    for i in range(diff.days+1):
        datelist.append((d1+td(days=i)).isoformat())
    for j in range(len(datelist)):
        datelist[j]=datelist[j].replace('-', '/')
    return datelist
        
datelist=dates()

for k in range(len(datelist)):
    file=open(datelist[k]+'.txt', "w")
    try:
        newslist=getnews('http://echo.msk.ru/news/'+datelist[k]+'.html')
        datelist[k]=datelist[k].replace('/', '-')
        for n in range(1, len(newslist)):
            file.write(newslist[n].text+'[newsbreak] \n')
        print(datelist[k]+' Done...')
        file.close()
    except Exception:
        file.close()
        continue
