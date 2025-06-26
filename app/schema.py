import strawberry
from app.resolvers.user_resolvers import QueryUser
from app.resolvers.post_resolvers import QueryPost, MutationPost

@strawberry.type
class Query(QueryUser, QueryPost):
    """Root query type that combines user and post queries."""
    pass

@strawberry.type
class Mutation(MutationPost):
    """Root mutation type that combines post mutations."""
    pass

schema = strawberry.Schema(query=Query, mutation=Mutation)