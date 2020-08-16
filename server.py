from flask import Flask, redirect, Response, request, url_for
from oauthlib.oauth1 import OAuth1Error
from urllib.parse import urlparse
from oauthlib.oauth1 import ResourceEndpoint
from .provider import server as provider
from .validators import MyRequestValidator
import functools

app = Flask(__name__)


@app.route('/request_token', methods=['POST'])
def request_token():
    h, b, s = provider.create_request_token_response(request.url,
            http_method=request.method,
            body=request.data,
            headers=dict(request.headers))
    return Response(b, status=s, headers=h)


# @app.route('/authorize', methods=['GET'])
# def pre_authorize():
#     realms, credentials = provider.get_realms_and_credentials(request.url,
#             http_method=request.method,
#             body=request.data,
#             headers=request.headers)
#     client_key = credentials.get('resource_owner_key', 'unknown')
#     response = '<h1> Authorize access to %s </h1>' % client_key
#     response += '<form method="POST" action="/authorize">'
#     for realm in realms or []:
#         response += ('<input type="checkbox" name="realms" ' +
#                         'value="%s"/> %s' % (realm, realm))
#     response += '<input type="submit" value="Authorize"/>'
#     return response


# @app.route('/authorize', methods=['POST'])
# def post_authorize():
#     print('enter2')
#     realms = request.form.getlist('realms')
#     try:
#         h, b, s = provider.create_authorization_response(request.url,
#                 http_method=request.method,
#                 body=request.data,
#                 headers=request.headers,
#                 realms=realms)
#         if s == 200:
#             return 'Your verifier is: ' + str(urlparse.parse_qs(b)['oauth_verifier'][0])
#         else:
#             return Response(b, status=s, headers=h)
#     except OAuth1Error as e:
#         return redirect(e.in_uri(url_for('/error')))


@app.route('/access_token', methods=['POST'])
def access_token():
    h, b, s = provider.create_access_token_response(request.url,
            http_method=request.method,
            body=request.data,
            headers=dict(request.headers))
    return Response(b, status=s, headers=h)


@app.route('/error', methods=['GET'])
def error():
    # Invalid request token will be most likely
    # Could also be an attempt to change the authorization form to try and
    # authorize realms outside the allowed for this client.
    return 'client did something bad'



def oauth_protected(realms=None):
    def wrapper(f):
        @functools.wraps(f)
        def verify_oauth(*args, **kwargs):
            validator = MyRequestValidator()  # your validator class
            provider = ResourceEndpoint(validator)
            v, r = provider.validate_protected_resource_request(request.url,
                    http_method=request.method,
                    body=request.data,
                    headers=dict(request.headers),
                    realms=realms or [])
            if v:
                return f(*args, **kwargs)
            else:
                return 'forbbiden', 403
        return verify_oauth
    return wrapper

@app.route('/secret', methods=['GET'])
@oauth_protected()
def protected_resource():
    return 'highly confidential'
