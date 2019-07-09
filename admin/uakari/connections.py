from django.conf import settings

import redis

r = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)
