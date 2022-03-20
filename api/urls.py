from .views import *
from django.urls import path


urlpatterns = [
    path('api/products', getAllProducts.as_view()),
    path('api/products/<int:pk>', getProduct.as_view()),
    path('api/profiles', getAllProfiles.as_view()),
    path('api/profiles/<int:pk>', getProfile.as_view()),
    path('api/add', addProduct.as_view())
]