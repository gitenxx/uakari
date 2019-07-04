from django.utils import timezone
from uakari.connections import r
from uakari.uakari import logger


def write_to_redis(df, expiration_time, rec_id):
    exp_time = expiration_time - timezone.now()
    for i in df:
        r.setex(i['short_url'], exp_time, i['long_url'])
    logger.info(f'All is written to redis, id: {rec_id}')


def write_one_url(short_url, long_url, expiration_time):
    exp_time = expiration_time - timezone.now()
    r.setex(short_url, exp_time, long_url)
