import requests as re

url = "http://m.ip138.com/ip.asp?ip="
url2 = "https://www.ip138.com/"

try:
    r = re.get(url2)
    r.raise_for_status
    r.encoding = 'UTF-8'
    print('Done')
except:
    print('Error')
