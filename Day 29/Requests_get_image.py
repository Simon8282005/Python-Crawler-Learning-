import requests as re
import os

print(os.listdir())  # 输出文件下的目录
url = "http://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg"  # 图片网址
root = "Desktop/"  # 保存图片的文件位置
path = root + url.split('/')[-1]  # 获得图片的原名（XXX.jpg）来作为图片的名字
print('Paht: ',path)

try:
    # 如果保存图片的文件夹不存在，创建一个名为 Desktop 的文件夹
    if not os.path.exists(root):
        os.mkdir(root)
    # 如果文件夹存在，但图片不存在，就从网上把图片爬取下来
    if not os.path.exists(path):
        r = re.get(url)
        with open(path,'wb') as f:  # ‘wb’是可写入的意思
            f.write(r.content)  # r.content 是r所保存的信息（图片的二进制数据）
            f.close()
            print('Done !!!')
    else:
        print('File already exists')
except:
    print('Error')
