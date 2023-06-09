from main_app import db
from sqlalchemy.sql import func


# Match model
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
        """Return the string representing a match."""
        return f"{self.home_team_name} {self.home_score} - {self.away_score} {self.away_team_name}"


# Visit model
class Visit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_ip = db.Column(db.String(15), unique=False)
    page_name = db.Column(db.String(25))

    def __repr__(self):
        """Return the string representing a visit."""
        return "Page: {}".format(self.page_name)

    def update_visits(self, user_ip, pagename):
        """Add a visit to the database"""
        self.user_ip, self.page_name = user_ip, pagename
        db.session.add(self)
        db.session.commit()
