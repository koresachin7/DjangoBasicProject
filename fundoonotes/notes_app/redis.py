import redis


class Redis:
    def __init__(self):
        self.redis = redis.Redis(
            host='localhost',
            port=6379,
            )

    def redis_post(self,pk,data):
        return self.redis.set(pk,data)

    def redis_get(self, pk):
        return self.redis.get(pk)

    def redis_put(self, pk, data):
        return self.redis.set(pk, data)

    def redis_delete(self, pk):
        return self.redis.set(pk)
