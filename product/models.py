from django.db import models

# Create your models here.
class Product(models.Model):
    code = models.TextField(max_length=20, blank=False, null=False)
    name = models.TextField(max_length=250, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='products/', blank=True, null=True)
    qtt = models.IntegerField(blank=False, null=False)
    unity = models.TextField(max_length=3, blank=False, null=False)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=False, null=False)

    def __str__(self):
        return self.name