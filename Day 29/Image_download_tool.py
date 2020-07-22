import requests as re
import os

print(os.listdir())
url = input('Enter image url: ')
root = input('File name: ')
path = root + '/' + url.split('/')[-1]
print('Path: ',path)

try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = re.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close
            print('Done !!!')
    else:
        print('File already exists.')
except:
    print('Ooops ! Somethings went wrong.')
