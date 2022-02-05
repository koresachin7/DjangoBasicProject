import jwt, datetime


class UserViwe:
    @staticmethod
    def encode(payload):
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        return token

    @staticmethod
    def decode(token_encode):
        payload = jwt.decode(token_encode, 'secret', algorithms=['HS256'])
        return payload
