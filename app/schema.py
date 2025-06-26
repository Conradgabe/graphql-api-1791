import strawberry
from app.resolvers.user_resolvers import QueryUser, MutationUser
from app.resolvers.post_resolvers import QueryPost, MutationPost

# ---------------------------------------------
# Root Query Class
# Combines all individual query types into one.
# Strawberry supports inheritance-based composition,
# so we merge User and Post queries into a single Query root.
# ---------------------------------------------
@strawberry.type
class Query(QueryUser, QueryPost):
    """Root query type that combines user and post queries."""
    pass

# ---------------------------------------------
# Root Mutation Class
# Similar to Query, we combine all mutation types.
# This allows the GraphQL schema to support creating, updating,
# and deleting users and posts from a single Mutation root.
# ---------------------------------------------
@strawberry.type
class Mutation(MutationPost, MutationUser):
    """Root mutation type that combines post and user mutations."""
    pass

# ---------------------------------------------
# Final Schema Definition
# This is the entry point for Strawberry/Apollo/FastAPI
# to interpret your full GraphQL schema.
# ---------------------------------------------
schema = strawberry.Schema(query=Query, mutation=Mutation)
