import requests
from bs4 import BeautifulSoup

r = requests.get("https://news.tvbs.com.tw/news/searchresult/%E9%A3%9F%E5%AE%89/news") #將網頁資料GET下來

soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parse

a=soup.find_all(class_='search_list_box')

for title in a:
    #print(title.a["href"])
    news=title.find(class_='search_list_text')
    #print(x.h2.text)
    news_date=title.find(class_='publish_date display_none')
    #print(t.text)
    image=title.find("img",class_='lazyimage')
    #print(image["data-original"])
    if(image and news and news_date): 
        aa="圖片網址{image}\n新聞網址:{name}\n新聞標題:{news_titles}\n日期時間:{date}\n\n".format(name=title.a["href"],news_titles=news.h2.text,date=news_date.text,image=image["data-original"])
        print(aa)
        f = open("TVBS新聞網.txt",'a',encoding="UTF-8")  
        f.write(aa)
        f.seek(0)
        f.close()
        A=""

