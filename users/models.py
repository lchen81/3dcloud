from django.db import models

from applications.models import Application


class User(models.Model):
    name = models.CharField(max_length = 32, unique = True)
    email = models.CharField(max_length = 64, default="")
    password = models.CharField(max_length = 16)
    status = models.IntegerField(default = 0)

    applications = models.ManyToManyField(Application)

    def __str__(self):
        return self.name
