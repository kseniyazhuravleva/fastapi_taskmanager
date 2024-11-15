from fastapi import HTTPException

class UserNotFound(HTTPException):
    def __init__(self):
        self.status_code = 404
        self.detail = "sorry, but user not found!"

class InvalidPassword(HTTPException):
    def __init__(self):
        self.status_code = 404
        self.detail = "username or password is incorrect"