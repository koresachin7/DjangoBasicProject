import jwt, datetime


class JwtEnodeDecode:
    @staticmethod
    def encode(payload):
        """
        Description:
                This method is writing for encode data
        :return : Token
        """
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        return token

    @staticmethod
    def decode(token_encode):
        """
        Description:
                    This method is writing for decode data
        :return : payload
        """
        payload = jwt.decode(token_encode, 'secret', algorithms=['HS256'])
        return payload
