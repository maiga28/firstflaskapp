from main_apps.extensions import db
from datetime import datetime

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    like = db.Column(db.Integer, nullable=False, default=0)
    comment = db.Column(db.String(100), nullable=False, default=0)
    
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
