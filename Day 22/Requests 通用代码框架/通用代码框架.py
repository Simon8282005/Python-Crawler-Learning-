import requests

def getHTMLtext(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()  # 如果状态不是两百，引发HTTPError异常
        r.encoding = 'utf-8'  # 也可以这样写: r.encoding = r.apparent_encoding
        return r.text
    except:
        return '\n错误'

if __name__ == '__main__':
    url = 'http://www.baidu.com'
    print(getHTMLtext(url))
