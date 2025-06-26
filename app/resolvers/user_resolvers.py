import strawberry
from typing import List
from app.types.user_types import UserType
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User

@strawberry.type
class QueryUser:
    @strawberry.field
    def users(self) -> List[UserType]:
        """
        Resolver for fetching all users.
        This interacts with the database to retrieve all user data.
        """
        db: Session = next(get_db())
        return [UserType(id=user.id, name=user.name, email=user.email) for user in db.query(User).all()]
    
@strawberry.type
class MutationUser:
    @strawberry.mutation
    def create_user(self, name: str, email: str) -> UserType:
        """
        Resolver for Creating a User
        This interacts with the database to create user data.
        """
        try:
            db: Session = next(get_db())
            user = User(name=name, email=email)
            db.add(user)
            db.commit()
            db.refresh(user)
            return UserType(id=user.id, name=user.name, email=user.email)
        except Exception:
            raise Exception("Something unexpected happened: Email has already been taken")