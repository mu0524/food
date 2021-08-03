from flask import Flask, render_template, url_for,redirect
import  pymongo
# from bson.objectid import ObjectId
# import json


client = pymongo.MongoClient("mongodb+srv://admin:admin@mytopic.hpirm.mongodb.net/mytopicDB")
db = client.mytopicDB
coll = db.twpig #確認資料集
#coll = db.evaluation
#coll = db.free
#coll = db.green
coll.stats #確認是否連線

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') #return url string 中回傳index.html 做為模板

@app.route('/map.html')
def maptest():
    return render_template('map.html') 

@app.route('/news.html')
def news():
    return render_template('news.html') 

def connectdefult():
    b=coll.find_one({},{"addr": 1})
    print(b)
    addr=b["addr"]
    #如果獲取的資料為空
    if len(addr) == 0 :
        a={'message':"error!"}
        return jsonify(a)
    else:
        a={'message':"success!",'addr':addr}
        return jsonify(a)



@app.route('/green.html')
def green():
    return render_template('green.html') 

@app.route('/user.html')
def user():
    return render_template('user.html') 

@app.route('/login.html')
def login():
    return render_template('login.html') 

@app.route('/signin.html')
def signin():
    return render_template('signin.html') 

@app.route('/about.html')
def about():
    return render_template('about.html') 

@app.route('/index.html')
def test():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
