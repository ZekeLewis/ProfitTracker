from django.db import models

# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    sales = models.IntegerField()
    emp = models.IntegerField()
    tax = models.IntegerField()
    exp = models.IntegerField()
    expenses_monthly = models.IntegerField(default=0)
    income_monthly = models.IntegerField(default=0)