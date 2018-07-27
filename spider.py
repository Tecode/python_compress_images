import re
import requests

file = open('image.txt', 'r')
html = file.read()
file.close()

pic_url = re.findall('data-imgurl="(.*?)"', html, re.S)

index = 20
for img_url in pic_url:
  print(img_url)
  pic = requests.get(img_url)
  fileobj = open('./image/'+ str(index) + '.jpg', 'wb')
  fileobj.write(pic.content)
  fileobj.close
  index += 1