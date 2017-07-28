from bs4 import BeautifulSoup
import csv
import urllib2
import pandas as pd
import re

A = []
B = []
C = []
D = []
E = []

for i in range(1, 52):
    url = 'url'
    page = urllib2.urlopen(url)
    html = BeautifulSoup(page, 'html.parser')
    # print html
    link = html.findAll('a', {'itemprop' : 'name'})
    for a in range(len(link)):
        newurl = link[a].get('href')
        newpage = urllib2.urlopen(newurl)
        newhtml = BeautifulSoup(newpage, 'html.parser')
        name = newhtml.find('h1', {'itemprop': 'name'})
        # print name.string
        A.append(name.string.strip())

        adrs = newhtml.find('address', {'itemprop': 'address'})
        address = adrs.find('span').string
        B.append(address.strip())

        loc = newhtml.find('span', {'itemprop': 'addressRegion'})
        C.append(loc.string.strip())

        string = (newhtml.prettify(formatter=None))
        poss = string.find('"la":')
        lat = string[poss+5:poss+14]
        D.append(lat.strip())
    
        poss1 = string.find('"lo":')
        lon = string[poss1+5:poss1+14]
        E.append(lon.strip())
    
    
                        
#print A    
df = pd.DataFrame(A, columns=['Name'])
df['address'] = B
df['locality'] = C
df['latitude'] = D
df['longitude'] = E

df.to_csv('jammu/srinagar.csv',  encoding='utf-8')
    
