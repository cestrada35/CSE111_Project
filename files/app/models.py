# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Region(models.Model):
    """
    Model for Region
    """
    r_regionkey = models.AutoField(primary_key=True)
    r_name = models.CharField(max_length=25)

    class Meta:
        db_table = 'Region'


class Nation(models.Model):
    """
    Model for Nation
    """
    n_nationkey = models.AutoField(primary_key=True)
    n_name = models.CharField(max_length=25)
    n_regionkey = models.ForeignKey(
        Region, db_column='n_regionkey', on_delete=models.SET_NULL, blank=True, null=True
    )

    class Meta:
        db_table = 'Nation'


class Developer(models.Model):
    """
    Model for Developer
    """
    d_developer = models.CharField(max_length=34)
    d_doc = models.DateField()
    d_employees = models.IntegerField()
    d_networth = models.IntegerField()
    d_nationkey = models.ForeignKey(
        Nation, db_column='d_nationkey', on_delete=models.SET_NULL, blank=True, null=True
    )

    class Meta:
        db_table = 'Developer'


class Publisher(models.Model):
    """
    Model for Publisher
    """
    p_publisher = models.CharField(max_length=32)
    p_doc = models.DateField()
    p_employees = models.IntegerField()
    p_networth = models.IntegerField()
    p_nationkey = models.ForeignKey(
        Nation, db_column='p_nationkey', on_delete=models.SET_NULL, blank=True, null=True
    )

    class Meta:
        db_table = 'Publisher'


class Game(models.Model):
    """
    Model for Game
    """
    g_rank = models.DecimalField(max_digits=10, decimal_places=5)
    g_title = models.CharField(max_length=32)
    g_sales = models.TextField()
    g_genre = models.CharField(max_length=32)
    g_releasedate = models.DateField()
    g_platform = models.CharField(max_length=32)
    g_developer = models.ForeignKey(
        Developer, on_delete=models.SET_NULL, db_column='g_developer', blank=True, null=True
    )
    g_publisher = models.ForeignKey(
        Publisher, on_delete=models.SET_NULL, db_column='g_publisher', blank=True, null=True
    )

    class Meta:
        db_table = 'Game'


class Salestime(models.Model):
    """
    Model for Salestime
    """
    st_firstyear = models.IntegerField(blank=True, null=True)
    st_alltime = models.IntegerField(blank=True, null=True)
    st_game = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        db_table = 'SalesTime'
