from pydoc import describe
from rest_framework import serializers
from product.models import Product
from user.models import Profile


class ProductSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    seller = serializers.CharField(source='seller.name', max_length=255)
    price = serializers.IntegerField()
    describe = serializers.CharField(max_length=255)


class ProfileSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    raiting = serializers.IntegerField()
    is_salesman = serializers.BooleanField()
    verification = serializers.BooleanField()


class AddProduct(serializers.Serializer):
    seller = serializers.SlugRelatedField(slug_field="pk", queryset=Profile.objects)
    title = serializers.CharField(max_length=255)
    price = serializers.IntegerField()
    describe = serializers.CharField(max_length=255)

    def create(self, validated_data):
       return Product.objects.create(**validated_data)