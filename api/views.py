from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from product.models import Product
from user.models import Profile

from .serializers import ProductSerializer
from .serializers import ProfileSerializer


class getAllProducts(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer_for_queryset = ProductSerializer(
            instance=products,
            many=True
        )
        return Response(serializer_for_queryset.data)


class getAllProfiles(APIView):
    def get(self, request):
        profiles = Profile.objects.all()
        serializer_for_queryset = ProfileSerializer(
            instance=profiles,
            many=True
        )
        return Response(serializer_for_queryset.data)


class getProfile(APIView):
    def get(self, request, pk):
        profile = get_object_or_404(Profile, pk=pk)
        serializer_for_queryset = ProfileSerializer(
            instance=profile,
        )
        return Response(serializer_for_queryset.data)


class getProduct(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer_for_queryset = ProductSerializer(
            instance=product,
        )
        return Response(serializer_for_queryset.data)
