from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=30, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

CATEGORY = (
    ('Indoor', 'Indoor'),
    ('Outdoor', 'Outdoor'),
)

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=20, null=True, choices=CATEGORY)
    description = models.CharField(max_length=100, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

STATUS = (
    ('Pending', 'Pending'),
    ('Out for delivery', 'Out for delivery'),
    ('Delivered', 'Delivered'),
)

class Order(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=50, null=True, choices=STATUS)
    note = models.CharField(max_length=1000, null=True)

    def __str__(self):
        str_product = str(self.product)
        return str_product
