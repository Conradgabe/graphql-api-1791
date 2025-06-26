import strawberry
from app.types.user_types import UserType

# ------------------------------------------------------------
# GraphQL Type: PostType
# This defines the shape of a Post object returned in the API.
# Strawberry uses this class to auto-generate GraphQL schema types.
# ------------------------------------------------------------
@strawberry.type
class PostType:
    id: int        # Unique identifier of the post
    title: str     # Title of the post
    content: str   # Full content or body of the post
    author: UserType  # Nested user type representing the post's author
