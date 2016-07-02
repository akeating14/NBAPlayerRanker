from flask import render_template, Blueprint

player_ranker_blueprint = Blueprint(
    'data_forecast', __name__,
    template_folder='templates'
)


@player_ranker_blueprint.route('/')
def home():
    return render_template('base.html')
