from oauthlib.oauth1 import RequestValidator
from json import loads
from models import Test

class MyRequestValidator(RequestValidator):
    def validate_client_key(self, client_key, request):
        try:
            return True
        except:
            return False

    def check_verifier(self, verifier):
        return verifier

    def get_default_realms(self, client_key, request):
        return []

    def validate_timestamp_and_nonce(self, client_key, timestamp, nonce, request, request_token=None, access_token=None):
        return True

    def validate_requested_realms(self, client_key, realms, request):
        return True

    def validate_redirect_uri(self, client_id, redirect_uri, request):
        return True

    def validate_verifier(self, client_key, token, verifier, request):
        return True

    def get_client_secret(self, client_key, request):
        return 'foo'

    def save_request_token(self, token, request):
        return True

    def validate_request_token(self, client_key, token, request):
        return True

    def get_request_token_secret(self, client_key, token, request):
        return 'dummy'

    def get_realms(self, token, request):
        return ['currency', 'languages']

    def save_access_token(self, token, request):
        Test(id='5f35ff61a2e094667c438c21', access_token_secret=token['oauth_token_secret'], access_token=token['oauth_token']).save()

    def invalidate_request_token(self, client_key, request_token, request):
        pass

    def validate_access_token(self, client_key, token, request):
        return True

    def validate_realms(self, client_key, token, request, uri=None, realms=None):
        return True

    def get_access_token_secret(self, client_key, token, request):
        token = Test.objects.get(id='5f35ff61a2e094667c438c21').to_json()
        token = loads(token)
        return token['access_token_secret']
