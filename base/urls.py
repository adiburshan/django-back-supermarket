from django.contrib import admin
from django.db import router
from django.urls import include, path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, CategoryViewSet, ProductViewSet, CartViewSet, OrderDetailViewSet


router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'carts', CartViewSet)
router.register(r'orderdetails', OrderDetailViewSet)

urlpatterns = [
    path('' , views.index),
    path('register/' , views.register),
    path('login/', TokenObtainPairView.as_view()),
     path('', include(router.urls)),
]
