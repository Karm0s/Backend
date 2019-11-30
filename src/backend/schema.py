import graphene
from graphene_django import DjangoObjectType

from api.schema import Query as APIQuery

from accounts.schema import Query as AccountsQuery
from accounts.schema import Mutation as AccountsMutation

class Query(AccountsQuery, APIQuery, graphene.ObjectType):
    pass

class Mutation(AccountsMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)