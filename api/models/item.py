from operator import mod
from pyexpat import model
from statistics import mode
from django.db import models
from django.contrib.auth import get_user_model


class Item(models.Model):
  # define fields
  name = models.CharField(max_length=100)
  item_type = models.ForeignKey(
    'ItemType',
    on_delete=models.CASCADE,
    related_name='item_type_id'
  )
  concentration = models.IntegerField(null=True)
  conentration_units = models.CharField(max_length=20,null=True)
  volume = models.IntegerField(null=True)
  volume_units = models.CharField(max_length=20,null=True)
  description = models.TextField(null=True)
  category_id = models.ForeignKey(
    'Category',
    on_delete=models.CASCADE,
    related_name='category_id'
  )
  container_id = models.ForeignKey(
    'Container',
    on_delete=models.CASCADE,
    related_name='container_id'
  )
  owner = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
    null=True
  )
  manufacturer_id = models.ForeignKey(
    'Manufacturer',
    on_delete=models.CASCADE,
    related_name='manufacturer_id',
    null=True
  )
  storage_id = models.ForeignKey(
    'Storage',
    on_delete=models.CASCADE,
    related_name='storage_ID'
  )
  exp_id = models.ForeignKey(
    'Experiment',
    on_delete=models.CASCADE,
    related_name='exp_id',
    null=True
  )
