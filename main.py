from flask import Flask


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Hello Heroku :P"
#from appdir import routes

if __name__ == '__main__':
    app.run(threaded=True, port=5000)

