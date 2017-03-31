from __future__ import unicode_literals

from django.db import models


class Organizations(models.Model):
    org_name = models.CharField(max_length=200)
    org_phone = models.DecimalField(
        max_length=200, max_digits=14, decimal_places=4)
    org_email = models.EmailField(max_length=50)
    org_address = models.CharField(max_length=500)

    def __str__(self):
        return self.org_name + " " + str(self.org_phone) + " " + self.org_email + " " + self.org_address

