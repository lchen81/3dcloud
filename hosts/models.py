from django.db import models

from applications.models import Application


class Host(models.Model):
    name = models.CharField(max_length = 32, unique = True)
    ip = models.GenericIPAddressField(protocol = 'IPv4')
    mac = models.CharField(max_length=32)

    applications = models.ManyToManyField(Application)

    def __str__(self):
        return self.ip
