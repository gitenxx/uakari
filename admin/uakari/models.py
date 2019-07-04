from django_webdav_storage.storage import WebDavStorage

from django.db import models
from django.conf import settings
from uakari.tasks import file_process
from uakari.file_processing import URLProcessor
from uakari.uakari import logger


class Record(models.Model):
    Q = 'in queue'
    ST = 'starter'
    SC = 'success'
    F = 'failed'

    status_choices = ((Q, 'in queue'), (ST, 'started'), (SC, 'success'), (F, 'failed'))

    name = models.CharField(max_length=64)
    initial_file = models.FileField(upload_to='files/', blank=True)
    result_file = models.FileField(storage=WebDavStorage(), blank=True)
    status = models.CharField(max_length=64, blank=True, choices=status_choices)
    max_hash_length = models.IntegerField(default=24)
    expire_at = models.DateTimeField(null=True, blank=True)
    num_links = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'record edit'
        verbose_name_plural = 'records edit'

    def send_task(self):
        logger.info(f'Sending task to queue. Record id: {self.id}')
        self.status = self.Q
        self.save()
        file_process.apply_async([self.id, ])


class OneRecord(models.Model):

    long_url = models.CharField(max_length=225, blank=True)
    max_hash_length = models.IntegerField(default=24)
    expire_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        managed = False
        verbose_name = 'one record'
        verbose_name_plural = 'one record'

    def __str__(self):
        return self.long_url

    def write_to_redis(self):
        processor = URLProcessor()
        short_url = processor.process_url(self.long_url, self.max_hash_length, self.expire_at)
        return short_url

