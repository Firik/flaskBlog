from app import db


class BlogTag(db.Model):
    __tablename__ = 'blogs_tags'

    id = db.Column(db.Integer, primary_key=True)
    blog_id = db.Column(db.Integer, nullable=False)
    tag_id = db.Column(db.Integer, nullable=False)
