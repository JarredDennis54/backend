from .models import Categories
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    image=serializers.ImageField(allow_null=True)
    class Meta:
        model=Categories
        fields ='__all__'