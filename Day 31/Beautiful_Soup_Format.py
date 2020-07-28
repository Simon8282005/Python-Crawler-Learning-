import requests as re
from bs4 import BeautifulSoup as bs

try:
    r = re.get("http://python123.io/ws/demo.html")
    r.raise_for_status
    r.encoding = r.apparent_encoding
    demo = r.text
    soup = bs(demo, "html.parser")
    print(soup.prettify())
    print("----------------Complete---------------------------")
except:
    print('Error')
# http://python123.io/ws/demo.html
