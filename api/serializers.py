from rest_framework import serializers
from product.models import Product
from user.models import Profile


class ProductSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    seller = serializers.CharField(source='seller.name', max_length=255)
    price = serializers.IntegerField()
    describe = serializers.CharField()


class ProfileSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    raiting = serializers.IntegerField()
    is_salesman = serializers.BooleanField()
    verification = serializers.BooleanField()