from django.db import models

class Product(models.Model):
      no=models.IntegerField(primary_key=True)
      name=models.CharField(max_length=70)
      price=models.FloatField()
      quantity=models.IntegerField()
