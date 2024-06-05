from rest_framework import serializers
from .models import product,productCategory


class productserializers(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = '__all__'

class productCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = productCategory
        fields ='__all__'