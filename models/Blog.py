from app import db
from datetime import datetime


class Blog(db.Model):
    __tablename__ = 'blogs'

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    blog_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    caption = db.Column(db.String(150), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    dt_create = db.Column(db.DateTime, nullable=False, default=now)
    dt_change = db.Column(db.DateTime, default=now)

    def __init__(self, caption, description):
        self.caption = caption
        self.description = description
