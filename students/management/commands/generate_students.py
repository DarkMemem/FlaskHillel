from django.core.management.base import BaseCommand

from students.models import Students


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(nargs='+', type=int, dest='args')

    def handle(self, *args, **options):
        Students.generate_students(args[0])
