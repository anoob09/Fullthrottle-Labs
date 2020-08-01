from django.db import models

# Create your models here.
class User(models.Model):
    id = models.CharField(max_length=120, primary_key = True) 
    real_name = models.CharField(max_length=120)
    tz = models.CharField(max_length=120)


    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

class ActivityPeriod(models.Model):
    user = models.ForeignKey(User, verbose_name="User ID", on_delete=models.CASCADE)
    start_time = models.CharField(max_length=120)
    end_time = models.CharField(max_length=120)
    def __str__(self):
        return str(self.user)