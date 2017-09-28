from flask import Flask
from schema import Query
from flask_graphql import GraphQLView
from graphene import Schema
import os


view_func = GraphQLView.as_view(
    'graphql', schema=Schema(query=Query), graphiql=True)

app = Flask(__name__)
app.add_url_rule('/graphql', view_func=view_func)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
