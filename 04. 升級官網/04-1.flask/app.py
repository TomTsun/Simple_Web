import json
import bson.json_util as json_util
from flask import Flask, render_template, Response
with open('static/data.json',encoding="utf-8") as f:
    datas = json.load(f)
print(datas)
app = Flask(__name__)

@app.route('/index', methods={'POST','GET'})
def index():# 首頁
    return render_template('index.html', data = datas)

@app.route('/class/<number>')
def lecturer(number):
    return render_template('class.html', data = datas[int(number)])

@app.route('/api')
def api():
    return Response(
        response=json_util.dumps([datas]),
        mimetype='application/json')

@app.route('/')
def home():# 首頁
    return render_template('index.html', data = datas)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
    # app.run(host='0.0.0.0', port=8080)