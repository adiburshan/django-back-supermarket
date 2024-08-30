from django.db import models
from django.contrib.auth.models import User

# Customer model
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

# Category model
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_type = models.CharField(max_length=100)

    def __str__(self):
        return self.category_type

# Product model
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.description

# Cart model
class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart {self.cart_id} for {self.customer.user}"

# OrderDetail model
class OrderDetail(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.order_id} by {self.customer.user}"
