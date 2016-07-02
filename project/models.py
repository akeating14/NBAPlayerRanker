from project import db
from sqlalchemy import Column, Integer


class GameLog(db.Model):

    __tablename__ = "gamelog"

    id = Column(Integer, primary_key=True)
    gamelog_id = db.Column(db.Integer)
    season_id = db.Column(db.Integer)
    player_id = db.Column(db.Integer)
    game_id = db.Column(db.Integer)
    game_date = db.Column(db.Date)
    gap = db.Column(db.Integer)
    matchup = db.Column(db.String(128))
    wl = db.Column(db.String(64))
    min_ = db.Column(db.Integer)
    fgm = db.Column(db.Integer)
    fga = db.Column(db.Integer)
    fg_pct = db.Column(db.Float(4))
    fg3m = db.Column(db.Integer)
    fg3a = db.Column(db.Integer)
    fg3_pct = db.Column(db.Float(4))
    ftm = db.Column(db.Integer)
    fta = db.Column(db.Integer)
    ft_pct = db.Column(db.Float(4))
    oreb = db.Column(db.Integer)
    dreb = db.Column(db.Integer)
    reb = db.Column(db.Integer)
    ast = db.Column(db.Integer)
    stl = db.Column(db.Integer)
    blk = db.Column(db.Integer)
    tov = db.Column(db.Integer)
    pf = db.Column(db.Integer)
    pts = db.Column(db.Integer)
    plus_minus = db.Column(db.Integer)
    names = db.Column(db.String(128))
    birthdate = db.Column(db.Date)
    age = db.Column(db.Integer)
    home = db.Column(db.String(64))
    away = db.Column(db.String(64))
    team = db.Column(db.String(64))
    op = db.Column(db.String(64))
    dk_pts = db.Column(db.Float(4))

    def __init__(self, gamelog_id, season_id, player_id,
                 game_id, game_date, gap, matchup, wl, min_, fgm,
                 fga, fg_pct, fg3m, fg3a, fg3_pct, ftm, fta, ft_pct, oreb,
                 dreb, reb, ast, stl, blk, tov, pf, pts, plus_minus,
                 names, birthdate, age, home, away, team, op, dk_pts):

        self.gamelog_id = gamelog_id
        self.season_id = season_id
        self.player_id = player_id
        self.game_id = game_id
        self.game_date = game_date
        self.gap = gap
        self.matchup = matchup
        self.wl = wl
        self.min_ = min_
        self.fgm = fgm
        self.fga = fga
        self.fg_pct = fg_pct
        self.fg3m = fg3m
        self.fg3a = fg3a
        self.fg3_pct = fg3_pct
        self.ftm = ftm
        self.fta = fta
        self.ft_pct = ft_pct
        self.oreb = oreb
        self.dreb = dreb
        self.reb = reb
        self.ast = ast
        self.stl = stl
        self.blk = blk
        self.tov = tov
        self.pf = pf
        self.pts = pts
        self.plus_minus = plus_minus
        self.names = names
        self.birthdate = birthdate
        self.age = age
        self.home = home
        self.away = away
        self.team = team
        self.op = op
        self.dk_pts = dk_pts
