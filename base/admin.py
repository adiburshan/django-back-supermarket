from django.contrib import admin
from .models import Cart, Category, Customer, OrderDetail, Product


admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(OrderDetail)




