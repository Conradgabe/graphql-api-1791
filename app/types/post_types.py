import strawberry
from app.types.user_types import UserType

@strawberry.type
class PostType:
    id: int
    title: str
    content: str
    author: UserType