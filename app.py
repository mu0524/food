from flask import Flask, render_template, url_for,redirect, request, jsonify
import  pymongo
import ssl
# from bson.objectid import ObjectId
# import json

# #coll = db.evaluation
# #coll = db.free
# #coll = db.green
# coll.stats #確認是否連線

app = Flask(__name__)

#連db
def connectdefult():
    client = pymongo.MongoClient("mongodb+srv://admin:admin@mytopic.hpirm.mongodb.net/mytopicDB", ssl=True,ssl_cert_reqs=ssl.CERT_NONE)
    db = client.mytopicDB
    coll = db.twpig #確認資料集
    b = coll.find_one({},{"addr": 1}) #抓資料
    return b
    # addr=b["addr"]
    # #如果獲取的資料為空
    # if len(addr) == 0 :
    #     a={'message':"error!"}
    #     return jsonify(a)
    # else:
    #     a={'message':"success!",'addr':addr}
    #     return jsonify(a)


@app.route('/')
def index():
    return render_template('index.html') #return url string 中回傳index.html 做為模板

@app.route('/map')
def maptest():
    return render_template('map.html', name=connectdefult()) #小小測試東西有沒有傳到網頁

@app.route('/news')
def news():
    return render_template('news.html') 

@app.route('/greenresturant')
def green():
    return render_template('green.html') 

@app.route('/userinfo')
def user():
    return render_template('user.html') 

@app.route('/login', methods=['POST','GET']) #有表單(form)就需要methods這一個
def login():
    if request.method == 'POST': #請求method是post的資料
        if request.values['login-btn'] == 'login': #html頁面login按鈕 按鈕name的value等於login
            return redirect(url_for('index')) #跳轉至index function(前往index頁面)
    else:
        return render_template('login.html') 

@app.route('/signin')
def signin():
    return render_template('signin.html') 

@app.route('/about')
def about():
    return render_template('about.html') 

@app.route('/index.html')
def test():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
