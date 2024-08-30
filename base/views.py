from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import viewsets
from .models import Customer, Category, Product, Cart, OrderDetail
from .serializers import CustomerSerializer, CategorySerializer, ProductSerializer, CartSerializer, OrderDetailSerializer




@api_view(['GET'])
def index(req):
    return Response('hello')


# register
@api_view(['POST'])
def register(request):
    user=User.objects.create_user(
        username=request.data['username'],
        email=request.data['email'],
        password=request.data['password']
    )
    user.is_active = True
    user.is_staff = True
    user.save()
    return Response("new user is created")


#login
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import viewsets
from .models import Customer, Category, Product, Cart, OrderDetail
from .serializers import CustomerSerializer, CategorySerializer, ProductSerializer, CartSerializer, OrderDetailSerializer




@api_view(['GET'])
def index(req):
    return Response('hello')


# register
@api_view(['POST'])
def register(request):
    user=User.objects.create_user(
        username=request.data['username'],
        email=request.data['email'],
        password=request.data['password']
    )
    user.is_active = True
    user.is_staff = True
    user.save()
    return Response("new user is created")


#login
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

# CRUD:


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class OrderDetailViewSet(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer


# CRUD:


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class OrderDetailViewSet(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer

