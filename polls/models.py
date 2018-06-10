from django.contrib.auth.models import User
from django.db import models


# Create your models here.
# parent class
class Poll(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    text = models.CharField(max_length=200)
    publish_date = models.DateTimeField()

    def __str__(self):
        return self.text


# child class
class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    # votes = models.IntegerField(default=0)

    def __str__(self):
        return "{} - {}".format(self.poll.text[:25], self.choice_text[:25])
