from django.db import models
from users.models import User

# Create your models here.
class Person(models.Model):
  user_id = models.OneToOneField(User, on_delete=models.CASCADE, default=0)
  name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)

class Customer(models.Model):
  person_id = models.OneToOneField(Person, on_delete=models.CASCADE, default=0)
  is_active = models.BooleanField()
  is_deleted = models.BooleanField()

class Purchase(models.Model):
  customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
  iva = models.DecimalField(max_digits=10, decimal_places=2)
  subtotal = models.DecimalField(max_digits=10, decimal_places=2)
  total = models.DecimalField(max_digits=10, decimal_places=2)

class Category(models.Model):
  name = models.CharField(max_length=200)
  description = models.TextField()

class Product(models.Model):
  category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
  name = models.CharField(max_length=200)
  description = models.TextField()
  quantity = models.IntegerField()
  price = models.DecimalField(max_digits=10, decimal_places=2)

class PurchaseProducts(models.Model):
  product_id = models.OneToOneField(Product, on_delete=models.PROTECT)
  purchase_id = models.OneToOneField(Purchase, on_delete=models.CASCADE)
  quantity = models.IntegerField()
