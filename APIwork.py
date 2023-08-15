from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>hello</h1>"
@app.route("/hello_world1")
def hello_world1():
    return "<h1>hello world</h1>"
@app.route("/")
def hello_world2():
    return "<h1>hello</h1>"
@app.route("/test")
def test():
    a=5+65
    return "this is my function{}".format(a)
@app.route("/test2/test2")
def test2():
    data = request.args.get('x')
    return '''this the data input {}'''.format(data)

if __name__=="__main__":
    app.run(host="0.0.0.0")
