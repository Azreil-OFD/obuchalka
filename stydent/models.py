from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=30)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name