import strawberry

# ------------------------------------------------------------
# GraphQL Type: UserType
# Defines the fields returned when querying a user.
# Used by Strawberry to build the GraphQL schema for User objects.
# ------------------------------------------------------------
@strawberry.type
class UserType:
    id: int      # Unique identifier of the user
    name: str    # Full name of the user
    email: str   # Email address of the user
