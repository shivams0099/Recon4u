from bs4 import BeautifulSoup
import requests
import json
def reverseip(url):

    reverse_ip=requests.post("https://domains.yougetsignal.com/domains.php", data={'remoteAddress':url})
    reverseips=reverse_ip.content
    soup=BeautifulSoup(reverseips, 'html.parser')
    #soup=soup.prettify()
    #print(soup)
    #temp=str(soup.find("message"))
    dic=json.loads(str(soup))
    #for k,v in dic.items():
        #print(k,":",v)
    values=dic["domainArray"]
    for i in values:
        t=str(i)
        t=t.split(",")
        t=str(t[0])
        print(t[2:len(t)-2])



reverseip("srmcem.ac.in")
