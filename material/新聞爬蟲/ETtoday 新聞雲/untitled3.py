import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.ettoday.net/news/tag/%E9%A3%9F%E5%AE%89/") #將網頁資料GET下來

soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parse

a=soup.find_all(class_='piece clearfix')

for title in a:
    news=title.find("h3")
    news_Introduction=title.find(class_='summary')
    news_date=title.find(class_='date') 
    image=title.find("img")
    if(image and news and news_date and news_Introduction):  
          aa="圖片網址{image}\n新聞網址:{name}\n新聞標題:{news_titles}\n段落簡介:{Introduction}\n日期時間:{date}\n\n".format(name=news.a["href"],news_titles=news.text,Introduction=news_Introduction.text,date= news_date.text,image=image["content"])
          print(aa)
          f = open(" ETtoday 新聞雲.txt",'a',encoding="UTF-8")
          f.write(aa)
          f.seek(0)
          f.close()
          A=""      
    
   # aa="新聞網址:{name}\n新聞標題:{news_titles}\n日期時間:{date}\n圖片網址{image}\n\n".format(name=title.a["href"],news_titles=x.h2.text,date=t.text,image=image["data-original"])
   # print(aa)

