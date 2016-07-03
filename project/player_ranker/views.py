from flask import render_template, Blueprint
from project.models import GameLog
from sqlalchemy import desc

player_ranker_blueprint = Blueprint(
    'data_forecast', __name__,
    template_folder='templates'
)


@player_ranker_blueprint.route('/home')
def home():
    best_log_object = GameLog.query.order_by(desc(GameLog.dk_pts)).limit(10).all()
    pts_log_object = GameLog.query.order_by(desc(GameLog.pts)).limit(10).all()
    return render_template('main.html', best_table=best_log_object,
                           pts_table=pts_log_object)
