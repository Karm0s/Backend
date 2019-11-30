from django.contrib.auth import get_user_model

import graphene
from graphene_django import DjangoObjectType

import graphql_jwt

class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()

class Query(graphene.ObjectType):
    users = graphene.List(UserType)

    def resolve_users(self, info, **kwargs):
        return get_user_model().objects.all()

class RegisterNewUserMutation(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        username = graphene.String(required=True)
        password = graphene.String(required=True)
    
    new_user = graphene.Field(UserType)

    def mutate(self, info, email, username, password):
        user_model = get_user_model()
        new_user = user_model(email=email, user_name=username)
        new_user.set_password(password)

        new_user.save()
        return RegisterNewUserMutation(new_user=new_user)

class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

    register_new_user = RegisterNewUserMutation.Field()
