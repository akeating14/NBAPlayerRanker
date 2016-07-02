from project import db
from sqlalchemy import Column, Integer

class GameLog(db.Model):

    __tablename__ = "gamelog"

    id = Column(Integer, primary_key=True)
    GAMELOG_ID = db.Column(db.Integer)
    SEASON_ID = db.Column(db.Integer)
    PLAYER_ID = db.Column(db.Integer)
    GAME_ID = db.Column(db.Integer)
    GAME_DATE = db.Column(db.Date)
    GAP = db.Column(db.Integer)
    MATCHUP = db.Column(db.String(128))
    WL = db.Column(db.String(64))
    MIN = db.Column(db.Integer)
    FGM = db.Column(db.Integer)
    FGA = db.Column(db.Integer)
    FG_PCT = db.Column(db.Float(4))
    FG3M = db.Column(db.Integer)
    FG3A = db.Column(db.Integer)
    FG3_PCT = db.Column(db.Float(4))
    FTM = db.Column(db.Integer)
    FTA = db.Column(db.Integer)
    FT_PCT = db.Column(db.Float(4))
    OREB = db.Column(db.Integer)
    DREB = db.Column(db.Integer)
    REB = db.Column(db.Integer)
    AST = db.Column(db.Integer)
    STL = db.Column(db.Integer)
    BLK = db.Column(db.Integer)
    TOV = db.Column(db.Integer)
    PF = db.Column(db.Integer)
    PTS = db.Column(db.Integer)
    PLUS_MINUS = db.Column(db.Integer)
    NAMES = db.Column(db.String(128))
    BIRTHDATE = db.Column(db.Date)
    AGE = db.Column(db.Integer)
    HOME = db.Column(db.String(64))
    AWAY = db.Column(db.String(64))
    TEAM = db.Column(db.String(64))
    OP = db.Column(db.String(64))
    DK_PTS = db.Column(db.Float(4))

    def __init__(self, GAMELOG_ID, SEASON_ID, PLAYER_ID,
                 GAME_ID, GAME_DATE, GAP, MATCHUP, WL, MIN, FGM,
                 FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM,FTA,FT_PCT, OREB,
                 DREB, REB, AST, STL, BLK, TOV, PF, PTS, PLUS_MINUS,
                 NAMES, BIRTHDATE, AGE, HOME, AWAY, TEAM, OP, DK_PTS):

        self.GAMELOG_ID = GAMELOG_ID
        self.SEASON_ID = SEASON_ID 
        self.PLAYER_ID = PLAYER_ID
        self.GAME_ID = GAME_ID
        self.GAME_DATE = GAME_DATE
        self.GAP = GAP
        self.MATCHUP = MATCHUP
        self.WL = WL 
        self.MIN = MIN
        self.FGM = FGM
        self.FGA = FGA
        self.FG_PCT = FG_PCT
        self.FG3M = FG3M
        self.FG3A = FG3M
        self.FG3_PCT = FG3_PCT
        self.FTM = FTM
        self.FTA = FTA
        self.FT_PCT + FT_PCT
        self.OREB = OREB
        self.DREB = DREB
        self.REB = REB
        self.AST = AST
        self.STL = STL
        self.BLK = BLK
        self.TOV = TOV
        self.PF = PF
        self.PTS = PTS
        self.PLUS_MINUS = PLUS_MINUS
        self.NAMES = NAMES
        self.BIRTHDATE = BIRTHDATE
        self.AGE = AGE
        self.HOME = HOME
        self.AWAY = AWAY
        self.TEAM = TEAM
        self.OP = OP
        self.DK_PTS = DK_PTS
