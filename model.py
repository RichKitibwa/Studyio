from flask_sqlalchemy import SQLAlchemy
from database import db

class TutorialInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    url = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<TutorialInfo {self.title}>'
