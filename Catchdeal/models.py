from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    attributes = models.ForeignKey('Attributes')
    categorys = models.ManyToManyField('Category', related_name='products')

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('title',)

class Attributes(models.Model):
    size = models.PositiveSmallIntegerField(blank=True, null=True)
    color = models.CharField(max_length=20, blank=True, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)

    def __unicode__(self):
        return '%s' % self.price

    class Meta:
        ordering = ('size',)

class Category(models.Model):
    title = models.CharField(max_length=30)

    def __unicode__(self):
        return self.title


