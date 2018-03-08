from flask import Flask
from flask import request
from datetime import datetime
from uadetector.flask import UADetector

app = Flask(__name__)
UADetector(app)
ctr = 1

@app.route('/')
def hello():
    return 'Hello!'


@app.route('/request')
def request_info():
    return f'request method: {request.method} url: {request.url} headers: {request.headers}'

@app.route('/now')
def now():
    now = datetime.utcnow()
    return f'{now}'

@app.route('/user-agent')
def userAgent():
    brow = request.user_agent.browser + request.user_agent.version
    return f' {request.ua.device_type} / {request.user_agent.platform} / {brow}   '

@app.route('/counter')
def counter():
    global ctr
    ctr += 1
    return f'counter: {ctr}'

if __name__ == '__main__':
    app.run(debug=True)
