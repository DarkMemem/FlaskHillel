from django.core.management.base import BaseCommand

from teachers.models import Teachers


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(nargs='+', type=int, dest='args')

    def handle(self, *args, **options):
        Teachers.generate_teachers(args[0])
