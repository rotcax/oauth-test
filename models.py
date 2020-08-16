from mongoengine import *

connect('auth-server')

# class Users():
#     name = StringField(max_length=300)
#     email = StringField(max_length=300, unique=True)
#     password = StringField(max_length=300)

# class Clients():
#     client_key = StringField(max_length=300)
#     client_secret = StringField(max_length=300)
#     rsa_key = StringField(max_length=300)
#     user = ReferenceField(Users)
#     realms = StringField(max_length=300)
#     default_realms = StringField(max_length=300)
#     redirect_uris = StringField(max_length=300)
#     default_redirect_uri = StringField(max_length=300)

# class RequestTokens():
#     client = ReferenceField(Clients)
#     user = ReferenceField(Users)
#     realms = StringField(max_length=300)
#     redirect_uris = StringField(max_length=300)
#     request_token = StringField(max_length=300)
#     request_token_secret = StringField(max_length=300)
#     verifier = StringField(max_length=300)

# class AccessTokens():
#     client = ReferenceField(Clients)
#     user = ReferenceField(Users)
#     realms = StringField(max_length=300)
#     access_token = StringField(max_length=300)
#     access_token_secret = StringField(max_length=300)

class Test(Document):
    access_token = StringField(max_length=300)
    access_token_secret = StringField(max_length=300)
