from django.db import models


class Application(models.Model):
    name = models.CharField(max_length = 32, unique = True)
    path = models.CharField(max_length = 256)

    def __str__(self):
        return self.name
