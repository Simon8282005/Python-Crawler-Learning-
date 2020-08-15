import requests
from bs4 import BeautifulSoup
import bs4

# 获得最好大学网的 HTML 源代码
def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 50)
        r.raise_for_status
        r.encoding = r.apparent_encoding
        return r.text 
    except:
        return ' '

# 将获得的源代码储存进一个名为 ulist列表里
def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string])

# 将 ulist 的内容打印出来，这里的 num 是要打印列表里多少个元素
def printUnivList(ulist, num):
    print('{:^10}\t{:^6}\t{:^10}'.format('排名', '学校名称', '总分'))
    for i in range(num):
        u = ulist[i]
        print('{:^1}\t{:^1}\t{:^1}'.format(u[0], u[1], u[2]))

def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20) # 首 20 个大学

main()