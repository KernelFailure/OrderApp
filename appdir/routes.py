#from appdir import app
# from main import app
from appdir import application as app


@app.route('/')
@app.route('/index')
def index():
    return "Hello Heroku :P \nFor real now"
