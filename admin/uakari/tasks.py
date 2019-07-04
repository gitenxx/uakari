from uakari.celery import celery_app
from uakari.file_processing import FileProcessor
from uakari.uakari import logger


@celery_app.task(queue='file_processing')
def file_process(record_id: int):
    from uakari.models import Record
    logger.info(f'Started task with record id: {record_id}')
    record = Record.objects.get(id=record_id)
    record.status = Record.ST
    record.save()

    try:
        processor = FileProcessor()
        record.result_file, record.num_links = processor.process_csv(record.initial_file, record.max_hash_length,
                                                                     record.expire_at, record_id)
        record.status = Record.SC
    except Exception:
        record.status = Record.F
        record.save()
        raise


    record.save()


