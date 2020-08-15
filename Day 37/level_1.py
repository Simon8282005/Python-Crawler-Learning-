import requests
from bs4 import BeautifulSoup

# 获得最好大学网的 HTML 源代码
def getHTMLText(url):
    return ''

# 将获得的源代码储存进一个名为 ulist列表里
def fillUnivList(ulist, html):
    pass

# 将 ulist 的内容打印出来，这里的 num 是要打印列表里多少个元素
def printUnivList(ulist, num):
    print('Suc' + str(num))

def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20) # 首 20 个大学

main()