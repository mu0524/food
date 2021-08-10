from flask import Flask, render_template, url_for,redirect, request, jsonify, flash
from pymongo import message
import dbController as db
import os
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

app = Flask(__name__)
app.secret_key = os.urandom(16).hex()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'
login_manager.login_message = '請先登入'


class User(UserMixin):
    pass

#確認使用者是否是在我們的合法清單users當中，若沒有，就什麼都不做。
#若有，就宣告一個我們剛才用UserMixin做出來的物件User()，貼上user標籤，
#並回傳給呼叫這個函數user_loader()的地方
@login_manager.user_loader
def user_loader(email): 
    users = db.selectUser(email)
    if email not in users:
        return
    user = User()
    user.id = email
    return user

@app.route('/')
def index():
    return render_template('index.html') #return url string 中回傳index.html 做為模板

@app.route('/map')
def maptest():
    data=db.selectPigdata()
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
        email = request.form['email_input']
        pwd = request.form['pwd_input']
        data = db.selectUserInfo(email)
        if pwd == data[2]:
            user = User()
            user.id = email
            uid = data[0]
            login_user(user)
            return redirect(url_for('login'),uid)
        else:
            return redirect(url_for('login'),alert='帳號密碼輸入錯誤')
        
        
        # if request.values['login-btn'] == 'login': #html頁面login按鈕 按鈕name的value等於login
        #     return redirect(url_for('index')) #跳轉至index function(前往index頁面)
    else:
        return render_template('login.html') 

@app.route('/signin', methods=["GET", "POST"])
def signin():
    if request.method == 'POST':
        email = request.form['email_input']
        users = db.selectUser(email)
        if len(users) == 0:
            userID = request.form['uid_input']
            pwd = request.form['pwd_input']
            if(db.insertUser(userID,email,pwd)):
                flash('註冊成功，請登入')
                return redirect(url_for('login'))
        else:
            flash('此email已註冊過，請重新輸入')
            return redirect(url_for('signin'))
    return render_template('signin.html') 

@app.route('/about')
def about():
    return render_template('about.html') 

@app.route('/index.html')
def test():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)