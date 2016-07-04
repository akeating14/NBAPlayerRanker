from flask import Blueprint
from flask_restful import Resource, reqparse, fields, marshal_with
from flask import request
from project.models import GameLog
from sqlalchemy import distinct
import ast

gamelog_api_blueprint = Blueprint('api', __name__)


class GameLog_Search(Resource):
    """
    TODO:1. Add the arguments to the reg parse
         2. Add a sorting mechnism
         3. 2 more endpoints for logs and just by
         4. Add tests
         Fun Fact: request.query_string, request.args.get('filter'), request.args
         are differnt ways to get data from the request.
    """
    resource_fields = {
                       'id ': fields.String,
                       'gamelog_id': fields.String,
                       'season_id': fields.String,
                       'player_id': fields.String,
                       'game_id': fields.String,
                       'game_date': fields.String,
                       'gap': fields.Integer,
                       'matchup': fields.String,
                       'wl': fields.String,
                       'min_': fields.Integer,
                       'fgm': fields.Integer,
                       'fga': fields.Integer,
                       'fg_pct': fields.Float(4),
                       'fg3m': fields.Integer,
                       'fg3a': fields.Integer,
                       'fg3_pct': fields.Float(4),
                       'ftm': fields.Integer,
                       'fta': fields.Integer,
                       'ft_pct': fields.Float(4),
                       'oreb': fields.Integer,
                       'dreb': fields.Integer,
                       'reb': fields.Integer,
                       'ast': fields.Integer,
                       'stl': fields.Integer,
                       'blk': fields.Integer,
                       'tov': fields.Integer,
                       'pf': fields.Integer,
                       'pts': fields.Integer,
                       'plus_minus': fields.Integer,
                       'names': fields.String,
                       'birthdate': fields.String,
                       'age': fields.Integer,
                       'home': fields.String,
                       'away': fields.String,
                       'team': fields.String,
                       'op': fields.String,
                       'dk_pts': fields.Float(4)}

    @marshal_with(resource_fields, envelope='resource')
    def get(self, **kwargs):
        q = GameLog.query
        arguments = request.args.get('filter')
        # parser = reqparse.RequestParser()
        # args = parser.parse_args()
        if request.args.get('limit') is None:
            return_size = 25
        else:
            return_size = request.args.get('limit')
        # arguments return as unicode, so I convert it to a dict
        if arguments:
            args = ast.literal_eval(arguments)

            for attr, value in args.items():
                """
                TODO: Apparently checking types is bad so I should try and replace this with
                duck typing
                """
                if isinstance(value, list):
                    q = q.filter(getattr(GameLog, attr).in_(value))
                else:
                    q = q.filter(getattr(GameLog, attr) == value)

        return q.limit(return_size).all()


class GameLog_Players(Resource):

    resource_fields = {
                       'player_id': fields.String,
                       'names': fields.String,
                       'birthdate': fields.String}

    @marshal_with(resource_fields, envelope='resource')
    def get(self, **kwargs):
        q = GameLog.query
        return q.distinct(GameLog.player_id).all()
