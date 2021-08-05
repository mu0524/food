import requests
from bs4 import BeautifulSoup

num=1
while(num<50):
   
 url ='https://greenliving.epa.gov.tw/newPublic/APIs/Restaurant4/%d'%num
 num=num+1
 response = requests.get(url)
 html = requests.get(url)
 html.encoding = 'UTF-8'
 sp = BeautifulSoup(html.text, 'html5lib')

#print(sp.h6.text)

 js_music = response.json()
 """
# 逐层展开字典，获得歌曲列表
 list_music = js_music['Detail']

# 遍历列表，得到每首歌曲的名称
 for music in list_music:
    f = open("test.txt",'a',encoding="UTF-8")  
    print("店名:",music['Name'],',地址:',music['Address'],',電話:',music['Phone'])
    a='"店名":{name},"地址":{Address},"電話":{Phone}\n"'.format(name=music['Name'],Address=music['Address'],Phone=music['Phone'])
    
    f.write(a)
    f.seek(0)
    f.close()
    
"""
print(js_music)