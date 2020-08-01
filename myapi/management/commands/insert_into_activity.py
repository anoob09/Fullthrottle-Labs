from django.core.management.base import BaseCommand
from django.utils import timezone
from myapi.models import User, ActivityPeriod
from django.utils.crypto import get_random_string
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = 'Insert random session into activity period table for a given UserId'
    
    def add_arguments(self, parser):
        parser.add_argument('userid', type=str, help='Userid for which dummy records are to be created')
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        userid = kwargs['userid']
        total = kwargs['total']
        user_obj = User.objects.filter(id = userid).values()
        if len(list(user_obj)) < 1:
            self.stdout.write(self.style.ERROR('User not present for userid = '"%s" % (userid)))
            return
        for i in range(total):
            now = datetime.now()
            end = now + timedelta(hours=1)
            start_time = now.strftime("%d/%m/%Y %H:%M:%S")
            end_time = end.strftime("%d/%m/%Y %H:%M:%S")
            temp = ActivityPeriod(user=userid, start_time = start_time, end_time = end_time)
            temp.save()
            self.stdout.write(self.style.SUCCESS('User "%s" deleted with success!'  (user_obj[0]["id"])))