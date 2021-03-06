from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_wtf.csrf import CsrfProtect
from flask_restful import Api
import os


app = Flask(__name__)
csrf = CsrfProtect(app)
db = SQLAlchemy(app)
api = Api(app)

app.config.from_object(os.getenv('APP_SETTINGS', 'config.ProductionConfig'))

from project.resources.gamelog import GameLog_Search, GameLog_Players

api.add_resource(GameLog_Search, '/api/v1/gamelogs/')
api.add_resource(GameLog_Players, '/api/v1/gamelogs/players/')



from project.player_ranker.views import player_ranker_blueprint
from project.resources.gamelog import gamelog_api_blueprint


app.register_blueprint(player_ranker_blueprint)
app.register_blueprint(gamelog_api_blueprint)