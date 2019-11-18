from bs4 import BeautifulSoup
import requests
def http_methods(url):
    text=requests.options(url)
    ##print(text.headers)
    print("Allowed HTTP Methods\n====================")
    if("Allow" in text.headers):
        print(text.headers["Allow"])
    else:
        print("Could not detect")

http_methods("http://aktu.ac.in")
