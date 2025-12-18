from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

# Association table for Many-to-Many (Posts-Tags)
post_tags = db.Table('post_tags',
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True)
)

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column (db.String(50), nullable=False)
    
    #One to many (User has many Posts)
    posts = db.relationship('Post', backref='user', lazy=True, cascade="all, delete-orphan")

    # Serialization rules: Include posts and their tags, but exclude backrefs to prevent recursion
    serialize_rules = ('-posts.user', '-posts.tags.posts')


class Post(db.Model, SerializerMixin):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column (db.String(100), nullable=False)
    content = db.Column (db.String(100), nullable=False)
    user_id = db.Column (db.Integer, db.ForeignKey('users.id'), nullable=False)

    # Many-to-Many: Post has many Tags (via association table)
    tags = db.relationship('Tag', secondary=post_tags, backref='posts', lazy=True)
    
    # Serialization rules: Exclude user (from One-to-Many) and tags.posts (to prevent recursion)
    serialize_rules = ('-user', '-tags.posts')

class Tag(db.Model, SerializerMixin):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    
    # Serialization rules: Include posts, but exclude the backref to prevent recursion
    serialize_rules = ('-posts.tags',)