from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    photo=models.ImageField(upload_to='upload', default='default.jpg')
    email=models.EmailField(max_length=254)
    password=models.CharField(max_length=10)
    phone_number=models.CharField(max_length=11)
    dateofbirth=models.DateField()

    def __str__(self):
        return self.name