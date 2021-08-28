from flask import Flask, render_template, url_for,redirect, request, flash, session
import dbController as db
import bcrypt

app = Flask(__name__)
mat = db.selectMaterial()
app.secret_key = mat['secret_key']
#app.permanent_session_lifetime = timedelta(minutes=20) session失效時間 


@app.route('/')
def index():
    if 'userID' in session:
        return render_template(('index.html'), uid = session['userID'])
    else:
        return render_template('index.html') #return url string 中回傳index.html 做為模板

@app.route('/map',methods=['POST','GET'])
def maptest():
    data= db.selectPigdata()
    greenData=db.selectGreenData()
    freeData=db.selectFreeData()
    Evaluation = db.marketFindComment()
    api = mat['map_api']

    if 'userID' in session:
        
        if request.method =='POST':
            keyWord=request.form['search_addr']
            data,greenData,freeData=db.myfind(keyWord)
        
        return render_template('map.html', uid = session['userID'],data=data, api=api, greenData=greenData, freeData=freeData, Evaluation=Evaluation)

    if request.method =='POST':
        keyWord=request.form['search_addr']
        data,greenData,freeData=db.myfind(keyWord)
    
    return render_template('map.html', data=data, api=api, greenData=greenData, freeData=freeData) #小小測試東西有沒有傳到網頁


#新增評價
@app.route('/map_Evaluation',methods=['POST','GET'])
def mapEvaluation():
    if request.method =='POST':
        userName = session['userID']
        comment = request.form['Evaluation_comment']
        market_name = request.values['Evaluation_name']
        db.insertComment(userName,comment,market_name)
        flash('評價成功','success')

    return redirect(url_for('maptest'))



@app.route('/news')
def news():
    ettoday = db.selectNews_ettoday()
    tvbs = db.selectNews_tvbs()
    udn = db.selectNews_udn()

    if 'userID' in session:
        return render_template(('news.html'), uid = session['userID'], etoday=ettoday, tvbs=tvbs, udn=udn)
    
    return render_template('news.html', etoday=ettoday, tvbs=tvbs, udn=udn) 

@app.route('/greenresturant')
def green():
    if 'userID' in session:
        return render_template(('green.html'), uid = session['userID'])
    return render_template('green.html') 

@app.route('/userinfo', methods=['POST','GET'])
def user():
    if request.method == 'POST':
        if request.values['logout-btn'] == 'logout': #html頁面login按鈕 按鈕name的value等於login
            session.clear()
            flash('您已登出','success')
            return redirect(url_for('index')) #跳轉至index function(前往index頁面)
    
    return render_template('user.html',uid = session['userID'])

@app.route('/changepwd', methods=["GET", "POST"])
def changepwd():
    if request.method == 'POST':
        newpwd = request.form['pwd_input']
        email = session['email']
        if newpwd == '':
            flash('請輸入密碼','warning')
            return redirect(url_for('index'))
        else:
            hashpass = bcrypt.hashpw(newpwd.encode('utf-8'), bcrypt.gensalt())
            db.updateUser(email,hashpass)
            flash('更改密碼成功','success')
            return redirect(url_for('index'))


@app.route('/login', methods=['POST','GET']) #有表單(form)就需要methods這一個
def login():
    if request.method == 'POST': #請求method是post的資料
        email = request.form['email_input']
        login_user = db.selectUser(email)
        if login_user :
            if bcrypt.hashpw(request.form['pwd_input'].encode('utf-8'), login_user['pwd']) == login_user['pwd']:
                session['email'] = email
                session['userID'] = login_user['userID']
                flash('登入成功','success')
                return redirect(url_for('index'))
            else:
                flash('帳號密碼輸入錯誤','error')
                return redirect(url_for('login'))
        else:
            flash('請先進行註冊','warning')
            return redirect(url_for('register'))

    return render_template('login.html') 

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        email = request.form['email_input']
        users = db.selectUser(email)
        if users is None:
            if email == '' or request.form['pwd_input'] == '':
                flash('請先輸入email及密碼','warning')
            else:
                userID = request.form['uid_input']
                hashpass = bcrypt.hashpw(request.form['pwd_input'].encode('utf-8'), bcrypt.gensalt())
                if(db.insertUser(userID,email,hashpass)):
                    session['userID'] = userID
                    session['email'] = email
                    flash('註冊成功，請登入','success')
                    return redirect(url_for('login'))
        else:
            flash('此email已註冊過，請重新輸入','error')
            return redirect(url_for('register'))
            
    return render_template('register.html') 

@app.route('/about')
def about():
    if 'userID' in session:
        return render_template(('about.html'), uid = session['userID'])
    else:
        return render_template('about.html') 

@app.route('/index.html')
def test():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)