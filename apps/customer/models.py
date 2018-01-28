from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, related_name='customer_profile')
    phone_number = models.CharField(max_length=11, null=True, blank=True)

    def __str__(self):
        return self.user.username
