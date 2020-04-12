#library import
import sys
from bs4 import BeautifulSoup
import requests
import socket
import json


#color codes
if sys.platform.lower().startswith(('os', 'win', 'darwin', 'ios')):
    # Colors shouldn't be displayed on Mac and Windows
    end = red = green = yellow = cyan = ''
else:
    red = '\033[31m'
    yellow = '\033[93m'
    end = '\033[0m'
    green = '\033[34m'
    cyan = '\033[36m'


#functions

#Recon4U banner function
def banner():
    print('''
    Tool for footprinting and scanning
    ''')
    print('''%s
     ██▀███  ▓█████  ▄████▄   ▒█████   ███▄    █ %s▓█▒  ▓█ %s █▓   ██ %s ++++++++++++++++++++++++++++++%s
    ▓██ ▒ ██ ▓█   ▀ ▒██▀ ▀█  ▒██▒  ██  ██ ▀█   █ %s██░  ██▒%s ██  ▓██▒ %s+Shivam Singh (1612210091)   +%s
    ▓██ ░▄█  ▒███   ▒██%sv1.0%s▄ ▒██░  ██ ▓██  ▀█ ▓█▒%s███████░%s ██  ▒██░ %s+Shubham Sharma (1612210100) +%s
    ▒██▀▀█▄  ▒██  ▄ ▒██▒ ▄██▒▒██   ██ ▓██▒  ▐▌██▒%s▒░░░░██░%s▓██  ░██░ %s+ CS-73                      +%s
    ░██▓ ▒██▒░█████▒▒ ████▀ ░░ █████▒░▒██░   ███░%s    ▒██░%s▒▓█████▓  %s+ Reconnaisance Tool         +%s
    ░ ▒▓ ░▒▓░░░ ▒░ ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ %s    ▒░▓ %s░▒▓▒ ▒ ▒  %s+                            +%s
      ░▒ ░ ▒░ ░ ░  ░  ░  ▒%sCoded by:@shivams0099%s░ ▒░  %s ░░%s ░░▒░ ░ ░  %s+ CSE, SRMGPC, Lucknow       +%s
      ░░   ░    ░   ░        ░ ░ ░ ▒     ░   ░  ░░    %s ░ %s ░░░ ░ ░  %s+                            +%s
       ░        ░  ░░ ░          ░ ░            ░%s      ░ %s   ░      %s++++++++++++++++++++++++++++++%s
    ''' % (red, cyan, red, green, red, cyan, red, green, red, yellow, red, cyan, red, green, red, cyan, red,
           green, red, cyan, red, green, red, cyan, red, green, red, yellow, red, cyan, red, green, red, cyan
                     , red, green, red, cyan, red, green, end))
    print('''
    ---------------------------------------------------------------------------
    |                                                                         |
    |                                                                         |
    ---------------------------------------------------------------------------
    ''')

#menu of the Recon4U
def menu():
    print('''
        +-------------------------------------------------+
                        List of Scan or Actions
        +-------------------------------------------------+
        Scanning Site or IP:
        [0] Basic Recon
        [1] WHOIS Lookup
        [2] Geo-IP Lookup
        [3] Grab Banner
        [4] HTTP Header
        [5] DNS Lookup
        [6] Subnet Calculator
        [7] NMAP Port Scan
        [8] Subdomain Scanner
        [9] Reverse IP Domain Checker
        [10] MX Lookup
        [11] Platform Identifier
        [12] HTTP Methods
        [A] Scan For Everything
        [B] Scan Another Website
        [U] Check For Update
        [Q] Quit!
        ''')

#Basic Recon function
def basic_recon(urlt,url):
    print("BASIC SCAN\n==========")
    sdata = requests.get(urlt+url)
    sdatac = sdata.content
    soup = BeautifulSoup(sdatac, 'lxml')
    stitle=str(soup.title.text)
    print("[+] Site Title: "+stitle)
    print("[+] IP Address: "+socket.gethostbyname(url))
    print("[+] Server: "+sdata.headers['Server'])
    print("[+] CMS: Coming Soon.....")
    if('CF-RAY' in sdata.headers):
        print("[+] Cloudflare: Detected")
    else:
        print("[+] Cloudflare: Not Detected")
    robots=requests.get(urlt + url + "/robots.txt")
    if(str(robots.status_code)=='200'):
        print("[+] Robots File: Found")
        print("========Start of content=========")
        print(BeautifulSoup(robots.text, 'html.parser'))
        print("========End of content===========")
    else:
        print("[+] Robots File: Not Found")

#GeoIP lookup function
def geoip_lookup(url):
    print("GEO IP LOOKUP\n=============")
    geoip=requests.get("https://api.hackertarget.com/geoip/?q="+url)
    geoip_data=geoip.content
    soup = BeautifulSoup(geoip_data, 'html.parser')
    soup=str(soup)
    temp=soup.split("\n")
    for i in temp:
        print("[i] ",i)

#HTTP Header function
def http_header(url):
    print("HTTP HEADER\n===========")
    site_header=requests.get("https://api.hackertarget.com/httpheaders/?q=" + url)
    site_headers=site_header.content
    soup=BeautifulSoup(site_headers, 'html.parser')
    soup = str(soup)
    temp = soup.split("\n")
    for i in temp[:len(temp)-2]:
        print("[i] ", i)

#DNS lookup function
def dns_lookup(url):
    print("DNS LOOKUP\n==========")
    text = requests.get("https://api.hackertarget.com/dnslookup/?q=" + url)
    texts = text.content
    soup = BeautifulSoup(texts, 'html.parser')
    print(soup)

#Subnet calculation function
def subnet_calc(url):
    print("SUBNET CALCULATION\n==================")
    subnet_data=requests.get("https://api.hackertarget.com/subnetcalc/?q=" + url)
    subnet_datas=subnet_data.content
    soup=BeautifulSoup(subnet_datas, 'html.parser')
    print(soup)

#nmap scan function
def nmap_scan(url):
    print("NMAP PORT SCAN\n==============")
    nmap_port=requests.get("https://api.hackertarget.com/nmap/?q=" + url)
    nmap_port_scan=nmap_port.content
    soup = BeautifulSoup(nmap_port_scan, 'html.parser')
    print(soup)

#subdomain enumeration function
def subdomain_enum(url):
    print("SUBDOMAIN ENUMERATION\n=====================")
    subdomain=requests.get("https://api.hackertarget.com/hostsearch/?q=" + url)
    subdomain_data=subdomain.content
    soup=BeautifulSoup(subdomain_data, 'html.parser')
    print(soup)

#reverse ip lookup function
def reverseip(url):
    reverse_ip=requests.post("https://domains.yougetsignal.com/domains.php", data={'remoteAddress':url})
    reverseips=reverse_ip.content
    soup=BeautifulSoup(reverseips, 'html.parser')
    dic=json.loads(str(soup))
    values=dic["domainArray"]
    print("Reverse IP Domain Check")
    print("=========================\n")
    for i in values:
        t=str(i)
        t=t.split(",")
        t=str(t[0])
        print(t[2:len(t)-1])
    print('\n=========================')

#whois lookup function
def whois(url):
    print("WHOIS LOOKUP\n============")
    whois_data=requests.get("https://www.whois.com/whois/" + url)
    whois_datas=whois_data.content
    soup=BeautifulSoup(whois_datas, 'html.parser')
    temp=soup.find('pre', class_="df-raw" )
    temp=(str(temp.text)).split("URL of the ICANN W")
    print("=========================Start of the content=================================")
    print(temp[0])
    print("==========================End of the content==================================")

#HTTP Methods Function
def http_methods(urlt,url):
    text=requests.options(urlt+url)
    print("Allowed HTTP Methods\n====================")
    if("Allow" in text.headers):
        print(text.headers["Allow"])
    else:
        print("Could not detect")
    print('\n')


