from validators import MyRequestValidator
from oauthlib.oauth1 import WebApplicationServer

validator = MyRequestValidator()
server = WebApplicationServer(validator)
