from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


# Create your models here.

# class Driver(models.Model):
#     user = models.OneToOneField(User, related_name='driver_profile')
#
#     dr_id = models.IntegerField(primary_key=True)
#     acc_num = models.IntegerField(unique=True)
#     father_name = models.CharField(max_length=10, blank=True, null=True)
#     national_code = models.IntegerField(unique=True)
#     is_ready_field = models.NullBooleanField(
#         db_column='Is_Ready?')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     address = models.CharField(max_length=30, blank=True, null=True)
#     name = models.CharField(max_length=15, blank=True, null=True)
#     family = models.CharField(max_length=16, blank=True, null=True)
#     lat = models.IntegerField(blank=True, null=True)
#     lng = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         db_table = 'driver_table'
#
#     def __str__(self):
#         return self.user.username
#
#
class Driver(models.Model):
    dr_id = models.IntegerField(primary_key=True)
    acc_num = models.IntegerField(unique=True)
    father_name = models.CharField(max_length=10, blank=True, null=True)
    national_code = models.IntegerField(unique=True)
    is_ready_field = models.NullBooleanField(db_column='Is_Ready?')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    address = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=15, blank=True, null=True)
    family = models.CharField(max_length=16, blank=True, null=True)
    lat = models.IntegerField(blank=True, null=True)
    lng = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'driver'


class VehicleTable(models.Model):
    plate_number = models.IntegerField(primary_key=True)
    colour = models.CharField(max_length=10, blank=True, null=True)
    model = models.CharField(max_length=10, blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    insurance_expiration = models.IntegerField()
    dr = models.ForeignKey(Driver, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicle_table'
