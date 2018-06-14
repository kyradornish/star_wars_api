from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
import os

app = Flask(__name__)
app.config.from_object(Config)

from app import routes

bootstrap = Bootstrap(app)
