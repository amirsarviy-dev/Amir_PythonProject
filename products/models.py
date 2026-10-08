from django.db import models
class Product(models.Model):
    name = models. CharField (max_length=50)
    description = models. CharField (max_length=300,null=True,blank=True)
    price = models.FloatField()
    count = models. IntegerField()
