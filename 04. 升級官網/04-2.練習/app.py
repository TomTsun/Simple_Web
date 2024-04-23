from flask import Flask, render_template
app = Flask(__name__)

@app.route('/index', methods={'POST','GET'})
def index():# 首頁
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
    # app.run(host='0.0.0.0', port=8080)