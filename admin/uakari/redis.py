from django.utils import timezone

from functools import reduce

from .connections import r
from .uakari import logger


def write_to_redis(df, expiration_time, rec_id):
    exp_time = expiration_time - timezone.now()
    for i in df:
        r.setex(i['short_url'], exp_time, i['long_url'])
    logger.info(f'All is written to redis, id: {rec_id}')


def write_one_url(short_url, long_url, expiration_time):
    exp_time = expiration_time - timezone.now()
    r.setex(short_url, exp_time, long_url)


def get_keys():
    return {
        key_from_lst.decode(): r.get(key_from_lst.decode()).decode()
        for key_from_lst in r.keys()
    }

def get_specific_key(spkey):
    return r.get(spkey).decode()

def get_expiration_time(key):
    return "%02d:%02d:%02d" % reduce(lambda ll,b : divmod(ll[0],b) + ll[1:], [(r.ttl(key),),60,60])

def delete_one_url(key):
    r.delete(key)
    return key

def delete_all_urls():
    r.flushdb()