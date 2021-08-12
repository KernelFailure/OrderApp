from flask import Flask

application = Flask(__name__)

from appdir import routes
