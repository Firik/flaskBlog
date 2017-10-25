from app import db


class Blog(db.Model):
    __tablename__ = 'blogs'

    blog_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    caption = db.Column(db.String(150), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    dt_create = db.Column(db.DateTime, nullable=False)
    dt_change = db.Column(db.DateTime, default='00-00-0000 00:00')

    def __init__(self, blog_id, caption, description, dt_create, dt_change):
        self.blog_id = blog_id
        self.caption = caption
        self.description = description
        self.dt_create = dt_create
        self.dt_change = dt_change
