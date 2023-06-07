from main_app import db
from sqlalchemy.sql import func


class Match(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    home_team_id = db.Column(db.Integer(), unique=False)
    home_team_name = db.Column(db.String(100), unique=False)
    away_team_id = db.Column(db.Integer(), unique=False)
    away_team_name = db.Column(db.String(100), unique=False)
    home_score = db.Column(db.Integer(), default=0)
    away_score = db.Column(db.Integer(), default=0)
    date = db.Column(db.Date(), default=func.now())
    season = db.Column(db.String(9), unique=False)
    date_added = db.Column(db.DateTime(timezone=True), default=func.now())

    def __repr__(self):
        return f"{self.home_team_name} {self.home_score} - {self.away_score} {self.away_team_name}"