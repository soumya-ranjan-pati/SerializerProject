from pyexpat import model
from rest_framework import serializers
from myapp.models import Product

class ProductSerializer(serializers.ModelSerializer):
      class Meta:
            model=Product
            fields=['no','name','price','quantity']