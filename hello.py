from flask import Flask
app = Flask(__name__)

@app.route('/aaa')
def hello_world():
  return 'Hello, World!'

@app.route('/b2')
def hello_world2():
  return 'Hello, From b2!'