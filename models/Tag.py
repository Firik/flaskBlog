from app import db


class Tag(db.Model):
    __tablename__ = 'tags'

    tag_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
