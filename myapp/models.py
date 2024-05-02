from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200,null=True)
    price = models.IntegerField()
    category = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    rating = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=0)
    brand = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    img = models.ImageField(upload_to='static/media/')

    def __str__(self):
        return self.name