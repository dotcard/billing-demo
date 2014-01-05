from django.db import models

class Tariff(models.Model):
  tariffname = models.CharField(max_length = 100)
  price = models.IntegerField(default = 0)
  def __unicode__(self):
    return self.tariffname

class Customer(models.Model):
  fname = models.CharField(max_length = 50)
  lname = models.CharField(max_length = 50)
  gender = models.CharField(max_length = 1)
  tariff = models.ForeignKey(Tariff)
  def __unicode__(self):
    return '%s %s' % (self.fname, self.lname)

class Account(models.Model):
  money = models.DecimalField(max_digits = 9, decimal_places = 2)
  customer = models.ForeignKey(Customer)
  def __unicode__(self):
    return self.id, self.money
