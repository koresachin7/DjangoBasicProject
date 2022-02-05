import json

from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response

from notes_app.redis import Redis
from loghandler import logger
from users.utility import UserViwe


class RedisOperations:

    def post_to_cache(self, user_id, note_data):
        """
           Description:
                     this method is using cash data in redis DB
           :param : user_id, data
           :return: Redis cache data
        """
        try:
            notes_list = Redis().redis_get(user_id)
            if notes_list is None:
                Redis().redis.set(user_id, json.dumps([note_data]))
            else:
                notes_list = json.loads(notes_list)
                notes_list.append(note_data)
                Redis().redis.set(user_id, json.dumps(notes_list))
        except Exception as e:
            logger.error(e)
            raise e

    def get_to_cashe(self, user_id):
        """
            Description:
                    this method is using cash data in redis DB
            :param : user_id
            :return: Redis cache data
        """
        try:
            notes_list = Redis().redis.get(user_id)
            return notes_list
        except Exception as e:
            logger.error(e)
            raise e

    def put_to_cashe(self, user_id, update_data):
        """
            Description:
                    this method is using cash data in redis DB
            :param : user_id update_data
            :return: Redis cache update data
        """
        note_list = Redis().redis_get(user_id)
        load_list = json.loads(note_list)
        if load_list is None:
            Redis().redis.set(user_id, json.dumps([update_data]))
            return
        for note in load_list:
            if update_data.get("id") == note.get("id"):
                note.update(update_data)
                Redis().redis.set(user_id, json.dumps(load_list))
                return
        else:
            raise ObjectDoesNotExist

    def delete_to_cashe(self, pk, user_id):
        """
           Description:
                    this method is using cash data in redis DB
            :param : pk user_id
            :return: Redis delete update data
        """
        note_list = Redis().redis.get(user_id)
        load_list = json.loads(note_list)
        print(load_list)
        if note_list is None:
            raise ObjectDoesNotExist
        count = 0
        for note in load_list:
            count += 1
            if note.get("id") == pk:
                load_list.pop(count - 1)
                Redis().redis.set(user_id, json.dumps(load_list))
                return
        else:
            raise ObjectDoesNotExist


def verify_token(function):
    def wrapper(self, request):
        if 'HTTP_AUTHORIZATION' not in request.META:
            resp = Response({'message': 'Token not provided in the header'})
            resp.status_code = 400
            logger.info('Token not provided in the header')
            return resp
        token = request.META['HTTP_AUTHORIZATION']
        user_id = UserViwe.decode(token)
        request.data.update({'user_id': user_id['user_id']})
        return function(self, request)

    return wrapper
