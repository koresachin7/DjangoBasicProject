import json
from notes_app.redis import Redis
from loghandler import logger


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

    def get_to_cash(self, user_id):
        """
            Description:
                    this method is using cash data in redis DB
            :param : user_id
            :return: Redis cache data
        """
        try:
            Redis().redis.get(user_id)
        except Exception as e:
            logger.error(e)
            raise e
