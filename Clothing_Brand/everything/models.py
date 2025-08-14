from django.db import models

# Create your models here.


class User_Model(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    dob = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    isadmin = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.user_id)


class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    quantity = models.DecimalField(max_digits=1000, decimal_places=2)
    rating = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    photo = models.CharField(max_length=100, default=None)
    description = models.CharField(max_length=500, default="No Description")
    product_type = models.BooleanField(default=0)
    # 0 for suits, 1 for tshirts

    def __str__(self):
        return str(self.product_id)


class Cart(models.Model):
    userID = models.DecimalField(max_digits=100, decimal_places=2)
    productID = models.DecimalField(max_digits=100, decimal_places=2)
    quantity = models.DecimalField(max_digits=1000, decimal_places=2)

    def __str__(self):
        return str(self.userID)
