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

    def save(self,):
        blog = Blog(self.caption, self.description)
        db.session.add(blog)
        db.session.commit()

    @staticmethod
    def get_blogs():
        return Blog.query.with_entities(Blog.caption, Blog.description, Blog.dt_create)