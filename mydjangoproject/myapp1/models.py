from django.db import models
from django.contrib.auth.models import User
from myapp2.models import Product
from myapp3.models import Account
# Create your models here.
class SalesOrder(models.Model):
    amount = models.IntegerField()
    description = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ManyToManyField(Product)
    account = models.OneToOneField(Account, on_delete=models.CASCADE, null=True)
