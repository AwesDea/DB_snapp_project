from __future__ import unicode_literals
from django.contrib.auth.models import User


# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models


class Customer(models.Model):
    phone_number = models.CharField(primary_key=True, max_length=10)
    gender = models.CharField(max_length=1)
    birthday = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=20, blank=True, null=True)
    credit = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'customer'


class DiscountTable(models.Model):
    name = models.CharField(unique=True, max_length=10)
    percentage = models.IntegerField()
    source = models.IntegerField()
    destinition = models.IntegerField()
    trv = models.ForeignKey('TravelTable', models.DO_NOTHING)

    class Meta:
        db_table = 'discount_table'
        unique_together = (('name', 'trv'),)


class Driver(models.Model):
    dr_id = models.IntegerField(primary_key=True)
    phone_number = models.CharField(max_length=10)
    acc_num = models.IntegerField(unique=True)
    father_name = models.CharField(max_length=10, blank=True, null=True)
    national_code = models.IntegerField(unique=True)
    is_ready_field = models.NullBooleanField(db_column='Is_Ready?')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    address = models.CharField(max_length=30, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'driver'


class Mont(models.Model):
    sup = models.ForeignKey('SupportTable', models.DO_NOTHING)
    plate_number = models.ForeignKey('VehicleTable', models.DO_NOTHING, db_column='plate_number')

    class Meta:
        db_table = 'mont'
        unique_together = (('sup', 'plate_number'),)


class Mont2(models.Model):
    sup = models.ForeignKey('SupportTable', models.DO_NOTHING)
    dr = models.ForeignKey(Driver, models.DO_NOTHING)

    class Meta:
        db_table = 'mont2'
        unique_together = (('sup', 'dr'),)


class Mont3(models.Model):
    sup = models.ForeignKey('SupportTable', models.DO_NOTHING)
    trv = models.ForeignKey('TravelTable', models.DO_NOTHING)

    class Meta:
        db_table = 'mont3'
        unique_together = (('sup', 'trv'),)


class SupportTable(models.Model):
    sup_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10, blank=True, null=True)
    family = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        db_table = 'support_table'


class TravelTable(models.Model):
    trv_id = models.IntegerField(primary_key=True)
    origin = models.CharField(max_length=20)
    destinition = models.CharField(max_length=20)
    number_2_dest = models.CharField(db_column='2_Dest', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    date = models.DateField()
    grade = models.IntegerField(blank=True, null=True)
    phone_number = models.ForeignKey(Customer, models.DO_NOTHING, db_column='phone_number', blank=True, null=True)
    plate_number = models.ForeignKey('VehicleTable', models.DO_NOTHING, db_column='plate_number', blank=True, null=True)
    dr = models.ForeignKey(Driver, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'travel_table'


class VehicleTable(models.Model):
    plate_number = models.CharField(primary_key=True, max_length=5)
    colour = models.CharField(max_length=10, blank=True, null=True)
    model = models.CharField(max_length=10, blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    insurance_expiration = models.DateField()
    dr = models.ForeignKey(Driver, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'vehicle_table'
