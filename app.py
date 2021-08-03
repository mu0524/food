from flask import Flask, render_template, url_for,redirect

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
