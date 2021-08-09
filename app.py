from flask import Flask, render_template, url_for,redirect, request, jsonify
import dbController as db
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') #return url string 中回傳index.html 做為模板

@app.route('/map')
def maptest():
    data=db.selectOneForTest()
    return render_template('map.html', data=data,count=len(data)) #小小測試東西有沒有傳到網頁

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
    app.run(debug=True)
