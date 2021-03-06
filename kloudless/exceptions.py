class KloudlessException(Exception):
    def __init__(self, message=None, response=None):
        if message is None and hasattr(self, 'default_message'):
            message = self.default_message

        self.error_data = {}
        self.status = None
        self.response = response

        if response is not None:
            self.status = response.status_code
            message += ' Error data: ' + response.text
            try:
                self.error_data = response.json()
            except ValueError:
                pass
            else:
                if 'id' in self.error_data:
                    message = '[Request ID: %s] %s' % (
                        self.error_data['id'], message)

        super(KloudlessException, self).__init__(message)

class APIException(KloudlessException):
    default_message = "Request failed."

class AuthenticationException(KloudlessException):
    default_message = (
        "Authentication failed. Verify the API Key you are using is "
        "correct.")

class AuthorizationException(KloudlessException):
    default_message = (
        "Authorization failed. Please double check that the API Key "
        "being used is correct.")

class RateLimitException(KloudlessException):
    default_message = (
        "Rate limiting encountered. Please try again later.")

    def __init__(self, *args, **kwargs):
        super(RateLimitException, self).__init__(*args, **kwargs)
        self.retry_after = None
        if self.response is not None and 'Retry-After' in self.response.headers:
            self.retry_after = float(self.response.headers['Retry-After'])

class ServerException(KloudlessException):
    default_message = (
        "An unknown error occurred! Please contact support@kloudless.com "
        "with the Request ID for more details.")

class ConfigurationException(Exception):
    pass
