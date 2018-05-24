from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 32)
    email = models.CharField(max_length = 64)
    password = models.CharField(max_length = 16)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.name
