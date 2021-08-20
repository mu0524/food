import requests
from bs4 import BeautifulSoup

r = requests.get("https://udn.com/search/tagging/2/%E9%A3%9F%E5%AE%89") #將網頁資料GET下來

soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parse


a=soup.find_all('div',class_='story-list__news')#取HTML標中的 <div class="story-list__news"></div> 存入a

for title in a:
     image=title.find(class_="lazyload")#取HTML標中的 <class="lazyload"> 資料存入image
     if(image):
       image= "圖片網址:"+image["data-src"]
    
     x=title.find(class_='story-list__text')
     if(x.text):
         news_title="新聞標題:"+x.a.text
         news="新聞文章網址:"+x.a["href"]
         Introduction="段落簡介:"+x.p.text
     t=title.find('time',class_='story-list__time')
     if(t):
       date="日期時間:"+t.text
     c=title.find('a',class_='story-list__cate btn btn-blue')
     
    
    
     if (image and news_title and news and Introduction and date): 
       A=str(image)+"\n"+str(news_title)+"\n"+str(news)+"\n"+str(Introduction)+"\n"+str(date)+"\n\n"
     
     print(A)
     f = open("聯合新聞網.txt",'a',encoding="UTF-8")  #打開聯合新聞網.txt
     f.write(A)#將資料寫入檔案
     f.seek(0)#設定游標在最後
     f.close()#關閉檔案
     A=""

