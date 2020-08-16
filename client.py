# import logging
# import oauthlib
# import sys
# oauthlib.set_debug(True)
# log = logging.getLogger('oauthlib')
# log.addHandler(logging.StreamHandler(sys.stdout))
# log.setLevel(logging.DEBUG)


from requests_oauthlib import OAuth1Session

key = 'abcdefghijklmnopqrstuvxyzabcde'
secret = 'foo'
verifier = 'w34o8967345'

authorization_base_url = 'http://127.0.0.1:5000/authorize'
request_token_url = 'http://127.0.0.1:5000/request_token'
access_token_url = 'http://127.0.0.1:5000/access_token'

oauth = OAuth1Session(key, client_secret=secret, callback_uri='http://127.0.0.1/cb', verifier=verifier)
fetch_req = oauth.fetch_request_token(request_token_url)

authorization_url = oauth.authorization_url(authorization_base_url)
parse_auth = oauth.parse_authorization_response(authorization_url)

fetch = oauth.fetch_access_token(access_token_url)

print(fetch)

r = oauth.get('http://127.0.0.1:5000/secret')
print(r.content)
