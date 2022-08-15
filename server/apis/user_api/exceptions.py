from rest_framework.exceptions import APIException

class NoAuthToken(APIException):
    status_code = 401
    default_detail = "No authentication token provided"

class InvalidAuthToken(APIException):
    status_code = 401
    default_detail = "Invalid authentication token provided"

class FirebaseError(APIException):
    status_code = 500
    default_detail = "The user provided with the auth token is not a valid Firebase user, it has no Firebase UID"