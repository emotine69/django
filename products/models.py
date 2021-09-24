from django.db import models
from django.db.models.fields import TextField
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)     #max_length = required
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(decimal_places=2,max_digits=10000) 
    summary = models.TextField(blank=False,null=False)
    feature = models.BooleanField(null=True,default=True)


    def get_absolute_url(self):
        # return f"/products/{self.id}/"
        return reverse("products:product-detail",kwargs={"id":self.id})