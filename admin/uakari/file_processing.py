from django.conf import settings
import base64
import hashlib
import datetime
from functools import partial
import pandas as pd
import requests
from uakari.save_to_redis import write_to_redis, write_one_url
from uakari.uakari import logger


class Processor:
    def make_hash(self, long_url: str, hash_length: int):
        """make unique hash for short url"""
        hasher = hashlib.md5(long_url.encode())
        bytes_hash = base64.urlsafe_b64encode(hasher.digest())[:hash_length]
        str_hash = bytes_hash.decode()
        return str_hash


class FileProcessor(Processor):
    def output_csv(self, data_frame: pd.DataFrame, filename: str):
        """save processed urls to csv"""

        csv_data = data_frame.to_csv(sep=';', index=False)
        r = requests.put(f'{settings.WEBDAV_URL}/{filename}',
                         data=csv_data)
        r.raise_for_status()

    def process_csv(self, initial_fileobj: object, hash_length: int, expiration_time: datetime, rec_id):
        """batch process urls from provided csv"""

        logger.info(f'Processing is started, id: {rec_id}')

        df = pd.read_csv(initial_fileobj, delimiter=';', encoding='utf-8-sig')
        df_size = len(df.index)
        logger.info(f'Link count: {df_size}, id: {rec_id}')
        df['short_url'] = df['long_url'].apply(partial(self.make_hash, hash_length=hash_length))
        dict_from_df = (df[['long_url', 'short_url']]).to_dict('records')
        write_to_redis(dict_from_df, expiration_time=expiration_time, rec_id=rec_id)

        filename = f'processed_{datetime.datetime.now().strftime("%Y-%m-%d_%H:%M")}.csv'

        self.output_csv(df, filename)

        return filename, df_size


class URLProcessor(Processor):

    def process_url(self, long_url: str, max_hash_length: int, expiration_time: datetime):
        logger.info(f'Processing is started, long url: {long_url}')

        short_url = self.make_hash(long_url, max_hash_length)
        write_one_url(short_url, long_url, expiration_time)
        return short_url

