from datetime import datetime, timezone, timedelta
import settings
import jwt


class Token:
    def __init__(self, id, username):
        self.private_key = settings.PRIVATE_KEY.key
        self.username = username
        self.id = id


    def __get_token_data(self, token_type='refresh'):
        iat = datetime.now(timezone.utc)

        data = {
            "id": self.id,
            "iat": iat,
        }

        if token_type == 'access':
            data['exp'] = iat + timedelta(minutes=60)
            data['username'] = self.username
            return data
        
        data['exp'] = iat + timedelta(days=30)
        return data
    

    def get_tokens(self):

        tokens = {
            "access_token": jwt.encode(self.__get_token_data(token_type='access'), self.private_key, algorithm="RS256"),
            "refresh_token": jwt.encode(self.__get_token_data(), self.private_key, algorithm="RS256")
        }

        return tokens
    