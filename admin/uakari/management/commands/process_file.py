from django.core.management import BaseCommand
from uakari.file_processing import FileProcessor


class Command(BaseCommand):
    def handle(self, *args, **options):
        f = FileProcessor()
        f.process_csv(initial_fileobj='/test_file.csv', expiration_time=6000, hash_length=6)
