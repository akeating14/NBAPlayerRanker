from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_wtf.csrf import CsrfProtect
import os

app = Flask(__name__)
csrf = CsrfProtect(app)
db = SQLAlchemy(app)


app.config.from_object(os.getenv('APP_SETTINGS', 'config.ProductionConfig'))

from project.player_ranker.views import player_ranker_blueprint


app.register_blueprint(player_ranker_blueprint)
