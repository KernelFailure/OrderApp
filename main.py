# from flask import Flask
from appdir import application

app = application


if __name__ == '__main__':
    app.run(threaded=True, port=5000)

