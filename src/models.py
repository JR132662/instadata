import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(16), unique =True, nullable=False)
    password = Column(Text,nullable=False)
    email = Column(String (16), unique=True, nullable=False)
    first_name = Column(String(255), nullable=false)
    last_name = Column(String(255), nullable=false)

class Followers(Base):
    __tablename__ = 'followers'
    user = relationship('User')
    user_from_id = Column(integer, ForeignKey('user.id'), nullable=True)
    user_to_id = Column(Integer, ForeignKey('user.id'), nullable=True)

class Post(base):
    __tablename__ = "media"
    id = Column(Integer, primary_key=true)
    user = relationship(User)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)

class Media(base):
    __tablename__ = "media"
    id = Column(Integer, primary_key=True)
    mediatype = Column(Enum)
    url = Column(String)
    post = relationship(Post)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=True)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')