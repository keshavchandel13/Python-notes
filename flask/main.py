from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return "<p> Hello World </p>"
@app.route('/home')
def h():
    return '<h1>This is home page</h1>'
if __name__=='__main__':
    app.run()
