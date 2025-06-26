from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base  # Base is the declarative base for SQLAlchemy models

# -------------------------------
# User Model
# Represents a user in the system.
# Each user can have multiple posts (one-to-many relationship).
# -------------------------------
class User(Base):
    __tablename__ = 'users'  # Database table name

    id = Column(Integer, primary_key=True, index=True)  # Unique ID for the user
    name = Column(String)  # User's name
    email = Column(String, unique=True, index=True)  # Unique email with indexing

    # Relationship to Post model (1 user → many posts)
    posts = relationship("Post", back_populates="author")


# -------------------------------
# Post Model
# Represents a blog post or article.
# Each post belongs to one user (many-to-one relationship).
# -------------------------------
class Post(Base):
    __tablename__ = 'posts'  # Database table name

    id = Column(Integer, primary_key=True, index=True)  # Unique ID for the post
    title = Column(String)  # Title of the post
    content = Column(Text)  # Post content (can be large)

    author_id = Column(Integer, ForeignKey("users.id"))  # Foreign key to the user table

    # Relationship back to User model (many posts → 1 author)
    author = relationship("User", back_populates='posts')
