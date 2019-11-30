import graphene
from graphene_django import DjangoObjectType

from api.schema import Query as APIQuery
from accounts.schema import Query as AccountsQuery

class Query(AccountsQuery, APIQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)