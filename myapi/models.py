from django.db import models

# Create your models here.
# User is the main table having 3 id (Primary Key), real_name and tz as columns.
# I assumed the relation between two tables is one-to-many where one record from User is 
# related to many records from ActivityPeriod since a user can have more then one session.
# I believe this is the best way to store data by preserving the relationship between models.
# The id field in User is Foreign Key to user field in ActivityPeriod. 

class User(models.Model):
    id = models.CharField(max_length=120, primary_key = True) 
    real_name = models.CharField(max_length=120)
    tz = models.CharField(max_length=120)


    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

class ActivityPeriod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.CharField(max_length=120)
    end_time = models.CharField(max_length=120)
    def __str__(self):
        return str(self.user)