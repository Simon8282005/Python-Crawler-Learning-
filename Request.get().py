import requests as re

# r 是response对象，包含从服务器获得的所有信息
r = re.get('https://www.baidu.com')  
print(r.status_code)  # 200, 如果不是200则代表访问失败
# print(r.headers)  # 获取‘头部’信息
print(r.text)  # 获得内容，都是乱码
print(r.encoding)  # 获得编码形式
print(r.apparent_encoding)  # 获得备选编码形式
print('\n------------------------ After Modified Encoding ------------------\n')
r.encoding = 'utf-8'  # 替换编码形式成utf-8
print(r.text)  # 才次输出，看看结果
