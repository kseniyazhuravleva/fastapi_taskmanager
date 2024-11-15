from datetime import datetime, timezone, timedelta
import settings
import jwt


class Token:
    def __init__(self, private_key):
        self.private_key = private_key
    

    def gen_token(self):
        iat = datetime.now(timezone.utc)
        exp = iat + timedelta(minutes=60)

        encoded = jwt.encode({
        "password": "somepass",
        "id": 123,
        "username": "maksous",
        "iat": iat,
        "exp": exp,
        }, self.private_key, algorithm="RS256")
        return encoded

token = Token(settings.PRIVATE_KEY.key)