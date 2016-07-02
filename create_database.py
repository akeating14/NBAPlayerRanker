from project import db
from project.models import GameLog
from sqlalchemy import create_engine
import pandas as pd
import os


def create_db():

    db.create_all()
    db.session.commit()


def add_gamelogs():

    logs = pd.read_csv('logs_sample.csv')
    ENGINE = create_engine(os.environ['DATABASE_URL'])
    logs.to_sql(name='gamelog', index=False, if_exists='append', con=ENGINE)

if __name__ == "__main__":
    create_db()
    add_gamelogs()
