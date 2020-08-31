from django.db import models

class ProductInfo(models.Model):
    productData = models.CharField(max_length=50)
    dfv = models.CharField(max_length=50)
    variation = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    sku = models.CharField(max_length=50)
    checks = models.CharField(max_length=50,default=0)
    
    price = models.IntegerField(default=0)
    schedule = models.CharField(max_length=50,default=0)
    stock = models.CharField(max_length=50)
    

    def __str__(self):
        return self.productData