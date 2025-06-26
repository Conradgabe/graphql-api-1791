import strawberry
from typing import List
from app.types.post_types import PostType
from app.types.user_types import UserType
from app.models import Post, User
from app.database import get_db
from sqlalchemy.orm import Session

@strawberry.type
class QueryPost:
    @strawberry.field
    def posts(self) -> List[PostType]:
        """
        Resolver for fetching all posts.
        This interacts with the database to retrieve all posts data.
        """
        db: Session = next(get_db())
        posts = db.query(Post).all()
        return [
            PostType(
                id=post.id,
                title=post.title,
                content=post.content,
                author=UserType(id=post.author.id, name=post.author.name, email=post.author.email)
            )
            for post in posts
        ]
    
    @strawberry.field
    def post(self, post_id: int) -> PostType:
        """
        Resolver for fetching a single post by ID.
        This interacts with the database to retrieve posts data.
        """
        db: Session = next(get_db())
        post = db.query(Post).filter(Post.id == post_id).first()
        if not post:
            raise Exception("Post not found")
        
        return PostType(
            id=post.id,
            title=post.title,
            content=post.content,
            author=UserType(id=post.author.id, name=post.author.name, email=post.author.email)
        )


@strawberry.type
class MutationPost:
    @strawberry.mutation
    def create_post(self, title: str, content: str, author_id: int) -> PostType:
        """
        Resolver for Creating a post
        This interacts with the database to create posts data.
        """
        db: Session = next(get_db())
        author = db.query(User).filter(User.id == author_id).first()
        if not author:
            raise Exception("Author not found")
        
        post = Post(title=title, content=content, author_id=author_id)
        db.add(post)
        db.commit()
        db.refresh(post)
        return PostType(
            id=post.id,
            title=post.title,
            content=post.content,
            author=UserType(id=author.id, name=author.name, email=author.email)
        )
    
    @strawberry.mutation
    def update_post(self, post_id: int, title: str = None, content: str = None) -> PostType:
        """
        Resolver for Updating a post
        This interacts with the database to update posts data.
        """
        db: Session = next(get_db())
        post = db.query(Post).filter(Post.id == post_id).first()
        if not post:
            raise Exception("Post not found")
        
        if title is not None:
            post.title = title
        if content is not None:
            post.content = content
        
        db.commit()
        db.refresh(post)
        
        return PostType(
            id=post.id,
            title=post.title,
            content=post.content,
            author=UserType(id=post.author.id, name=post.author.name, email=post.author.email)
        )
    
    @strawberry.mutation
    def delete_post(self, post_id: int) -> bool:
        """
        Resolver for deleting a post
        This interacts with the database to delete posts data.
        """
        db: Session = next(get_db())
        post = db.query(Post).filter(Post.id == post_id).first()
        if not post:
            raise Exception("Post not found")
        
        db.delete(post)
        db.commit()
        return True