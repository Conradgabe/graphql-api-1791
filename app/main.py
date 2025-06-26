from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from app.schema import schema

# Create a FastAPI application instance
app = FastAPI()

# Create a GraphQL router using the defined schema
graphql_app = GraphQLRouter(schema)

# Mount the GraphQL endpoint at /graphql
app.include_router(graphql_app, prefix="/graphql")