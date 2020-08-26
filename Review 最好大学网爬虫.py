import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
	try:
		r = requests.get(url, timeout = 50)
		r.raise_for_status
		r.encoding = 'utf-8'	
		return r.text
	except:
		return('Oooh ! Somethings went wrong.')

def fillUnivList(ulist ,html):
	soup = BeautifulSoup(html, "html.parser")
	for tr in soup.find('tbody'):
		if isinstance(tr, bs4.element.Tag):
			tds = tr('td')
			ulist.append([tds[0].string, tds[1].string, tds[2].string])

def printUnivList(ulist, num):
	tplt = '{0:^10}\t{1:{3}^10}\t{2:^10}'
	# tplt = '{:^10}\t{:{3}^6}\t{:^6}'
	print(tplt.format('排名','学校名称','地区', chr(12288)))
	for i in range(num):
		u = ulist[i]	
		print(tplt.format(u[0], u[1], u[2], chr(12288)))

def main():
	uinfo = []	
	url = input("Your url: ")
	html = getHTMLText(url)
	fillUnivList(uinfo, html)
	printUnivList(uinfo, 20)

main()
