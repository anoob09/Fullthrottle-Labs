from django.core.management.base import BaseCommand
from django.utils import timezone
from myapi.models import User
from django.utils.crypto import get_random_string

class Command(BaseCommand):
    help = 'Create random users add number of users as argument'
    
    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            userid = get_random_string()
            temp = User(id=userid, real_name = get_random_string(), tz=get_random_string())
            temp.save()
            self.stdout.write(self.style.SUCCESS('User "%s" added with success!' % (userid)))