import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        kv = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url, headers = kv,timeout = 50)
        r.raise_for_status
        r.encoding = 'utf-8'
        print(r.status_code)
        return r.text
    except:
        return ' '

def fillMoviesList(mlist, html):
    pass

def printMoviesList(mlist, num):
    print('Suc' + str(num))

def main():
    url = input("Please Type Your url: ")
    print(getHTMLText(url))

main()
