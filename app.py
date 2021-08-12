from flask import Flask, render_template, url_for,redirect, request, flash, session
from pymongo import message
import dbController as db
import os, bcrypt
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

app = Flask(__name__)
mat = db.selectMaterial()
app.secret_key = mat['secret_key']

# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.session_protection = 'strong'
# login_manager.login_view = 'login'
# login_manager.login_message = '請先登入'


# class User(UserMixin):
#     pass

# #確認使用者是否是在我們的合法清單users當中，若沒有，就什麼都不做。
# #若有，就宣告一個我們剛才用UserMixin做出來的物件User()，貼上user標籤，
# #並回傳給呼叫這個函數user_loader()的地方
# @login_manager.user_loader
# def user_loader(email): 
#     users = db.selectUser(email)
#     if email not in users:
#         return
#     user = User()
#     user.id = email
#     return user

@app.route('/')
def index():
    # if 'userID' in session:
    #     return render_template(('user.html'), uid = session['userID'])
    return render_template('index.html') #return url string 中回傳index.html 做為模板

@app.route('/map')
def maptest():
    data=db.selectPigdata()
    api = mat['map_api']
    return render_template('map.html', data=data, api=api) #小小測試東西有沒有傳到網頁

@app.route('/news')
def news():
    return render_template('news.html') 

@app.route('/greenresturant')
def green():
    return render_template('green.html') 

@app.route('/userinfo', methods=['POST','GET'])
def user():
    if request.method == 'POST':
        if request.values['logout-btn'] == 'logout': #html頁面login按鈕 按鈕name的value等於login
            session.clear()
            return redirect(url_for('index')) #跳轉至index function(前往index頁面)

    return render_template('user.html',uid = session['userID'])

@app.route('/login', methods=['POST','GET']) #有表單(form)就需要methods這一個
def login():
    if request.method == 'POST': #請求method是post的資料
        email = request.form['email_input']
        login_user = db.selectUser(email)
        if login_user :
            if bcrypt.hashpw(request.form['pwd_input'].encode('utf-8'), login_user['pwd']) == login_user['pwd']:
                session['email'] = email
                session['userID'] = login_user['userID']
                
                return redirect(url_for('user'))
            else:
                flash('帳號密碼輸入錯誤')
                return redirect(url_for('login'))
        else:
            flash('請先進行註冊')
            return redirect(url_for('signin'))

        # if email == data['email'] & pwd == data['pwd']:
        #     user = User()
        #     user.id = email
        #     uid = data['userID']
        #     login_user(user)
        #     return redirect(url_for('login'),uid)
        # else:
        #     return redirect(url_for('login'),alert='帳號密碼輸入錯誤')
        
        
        # if request.values['login-btn'] == 'login': #html頁面login按鈕 按鈕name的value等於login
        #     return redirect(url_for('index')) #跳轉至index function(前往index頁面)
    else:
        return render_template('login.html') 

@app.route('/signin', methods=["GET", "POST"])
def signin():
    if request.method == 'POST':
        email = request.form['email_input']
        users = db.selectUser(email)
        if users is None:
            userID = request.form['uid_input']
            hashpass = bcrypt.hashpw(request.form['pwd_input'].encode('utf-8'), bcrypt.gensalt())
            if(db.insertUser(userID,email,hashpass)):
                session['userID'] = userID
                session['email'] = email
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