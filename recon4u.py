import functions as f
import requests
import os
import json

while (1):
    f.banner()
    url = input("Enter the name of Website: ")
    try:
        urln = int(input("Enter 1 for http and 2 for https: "))
        urlt = ''
        if (urln == 1):
            urlt = "http://"
        elif (urln == 2):
            urlt = "https://"
        else:
            print("Invalid Input Please Re-enter")
            a = 1 / 0

        website = requests.get(urlt + url)

        print(website.status_code)
        f.menu()
        while (1):
            ch = input("[#] Choose Any Scan OR Action From The Above List: ")
            if (ch == '0'):
                print("[+] Scanning Begins..... \n[i] Scanning Site: " + urlt + url + "\n[S] Scan Type: Basic Recon")
                f.basic_recon(urlt, url)
            elif (ch == '1'):
                print("[+] Scanning Begins..... \n[i] Scanning Site: " + urlt + url + "\n[S] Scan Type: WHOIS Lookup")
                f.whois(url)
            elif (ch == '2'):
                print("[+] Scanning Begins..... \n[i] Scanning Site: " + urlt + url + "\n[S] Scan Type: Geo-IP Lookup")
                f.geoip_lookup(url)
            elif (ch == '3'):
                print("[+] Scanning Begins..... \n[i] Scanning Site: " + urlt + url + "\n[S] Scan Type: Grab Banner")
                print("coming soon......")
            elif (ch == '4'):
                print("[+] Scanning Begins..... \n[i] Scanning Site: " + urlt + url + "\n[S] Scan Type: HTTP Header")
                f.http_header(url)
            elif (ch == '5'):
                print("[+] Scanning Begins..... \n[i] Scanning Site: " + urlt + url + "\n[S] Scan Type: DNS Lookup")
                f.dns_lookup(url)
            elif (ch == '6'):
                print("[+] Scanning Begins..... \n[i] Scanning Site: " + urlt + url + "\n[S] Scan Type: Subnet Calculation")
                f.subnet_calc(url)
            elif (ch == '7'):
                print("[+] Scanning Begins..... \n[i] Scanning Site: " + urlt + url + "\n[S] Scan Type: NMAP Port Scan")
                f.nmap_scan(url)
            elif (ch == '8'):
                print("[+] Scanning Begins..... \n[i] Scanning Site: " + urlt + url + "\n[S] Scan Type: Subdomain Scanner")
                f.subdomain_enum(url)
            elif (ch == '9'):
                print("[+] Scanning Begins..... \n[i] Scanning Site: " + urlt + url + "\n[S] Scan Type: Reverse IP Domain Checker")
                f.reverseip(url)
            elif (ch == '10'):
                print("[+] Scanning Begins..... \n[i] Scanning Site: " + urlt + url + "\n[S] Scan Type: MX Lookup")
                print("Coming Soon.....")
            elif (ch == '11'):
                print("[+] Scanning Begins..... \n[i] Scanning Site: " + urlt + url + "\n[S] Scan Type: Platform Identifier")
                print("Coming Soon")
            elif (ch == '12'):
                print("[+] Scanning Begins..... \n[i] Scanning Site: " + urlt + url + "\n[S] Scan Type: Bucket Finder")
                f.http_methods(urlt,url)
            elif (ch == 'A' or ch == 'a'):
                print("[+] Scanning Begins..... \n[i] Scanning Site: " + urlt + url + "\n")
                f.basic_recon(urlt,url)
                print("\n")
                f.whois(url)
                print("\n")
                f.geoip_lookup(url)
                print("\n")
                f.http_header(url)
                print("\n")
                f.dns_lookup(url)
                print("\n")
                f.subnet_calc(url)
                print("\n")
                f.nmap_scan(url)
                print("\n")
                f.subdomain_enum(url)
                print("\n")
                f.reverseip(url)
                print("\n")
                f.http_methods(urlt,url)
                print('\n')
            elif (ch == "q" or ch == 'Q'):
                break
            elif (ch == "b" or ch == "B"):
                a = 1 / 0
            elif (ch == 'u' or ch == 'U'):
                print("No Updates Available....")
        break
    except(ZeroDivisionError):
        os.system("cls")
    except(Exception):
        print("Invalid Site Please Re-enter")

