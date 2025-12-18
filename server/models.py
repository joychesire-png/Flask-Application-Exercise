from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData()
db = SQLAlchemy(metadata=metadata)

class User(db.model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, Primary_key=True)
    name = db.Column (db.String(50), nullable=False)


class Post(db.model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, Primary_key=True)
    title = db.Column (db.String(100), nullable=False)
    content = db.Column (db.String(100), nullable=False)
    user_id = db.Column (db.Integer, db.ForeignKey('users.id'), nullable=False)

