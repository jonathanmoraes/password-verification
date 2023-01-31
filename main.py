from typing import Union

from fastapi import FastAPI
from schema import Query
from strawberry.asgi import GraphQL
import strawberry

app = FastAPI()


@app.get("/")
def read_root():
    return


schema = strawberry.Schema(query=Query)

graphql_app = GraphQL(schema)

app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)
