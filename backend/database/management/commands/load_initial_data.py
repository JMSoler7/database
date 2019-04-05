from django.core.management.base import BaseCommand
from dejavu_base.tests.factories import UserFactory


class Command(BaseCommand):
    help = 'Load initial fake data'

    def handle(self, *args, **options):
        UserFactory(username='staff', password='staff', is_superuser=True)
        UserFactory(username='basic', password='basic', is_staff=False)

        # Create fake data HERE

        self.stdout.write(self.style.SUCCESS('Fake data correctly created.'))
        self.stdout.write('-> Use staff/staff or basic/basic user')
