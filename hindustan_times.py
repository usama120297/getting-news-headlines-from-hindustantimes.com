import bs4 as bs
import csv
from urllib.request import Request, urlopen 
import re


f=open('news-headings.csv','w',newline='')
thewriter = csv.writer(f)

req = Request('https://www.hindustantimes.com/', headers={'User-Agent': 'Mozilla/5.0'})
sauce = urlopen(req).read()
soup = bs.BeautifulSoup(sauce,'lxml')
for url in soup.find_all('h2'):
    if url.text.strip():
        t1=url.text.strip().encode('ascii','ignore')
        thewriter.writerow([t1.decode().replace("b'","")])

for url in soup.find_all('h3'):
    if url.text.strip():
        t2=url.text.strip().encode('ascii','ignore')
        thewriter.writerow([t2.decode().replace("b'","")])

for url in soup.find_all('div',class_="media-heading headingfour"):
    if url.text.strip():
        t3=url.text.strip().encode('ascii', 'ignore')
        thewriter.writerow([t3.decode().replace("b'","")])

for url in soup.find_all('div',class_="media-heading headingfive"):
    if url.text.strip():
        t4=url.text.strip().encode('ascii', 'ignore')
        thewriter.writerow([t4.decode().replace("b'","")])


for url in soup.find_all('div',class_="para-txt"):
    if url.text.strip():
        t5=url.text.strip().encode('ascii', 'ignore')
        thewriter.writerow([t5.decode().replace("b'","").replace("Follow us on:","").replace("Register with Hindustan Times to get best news and articles","")])

f.close()
