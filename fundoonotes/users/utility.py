import jwt, datetime


class UserViwe:
    @staticmethod
    def encode(id):
        payload = {
            'user_id': id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        return token

    @staticmethod
    def decode(token_encode):
        payload = jwt.decode(token_encode, 'secret', algorithms=['HS256'])
        return payload
