from django.db import models

class Product(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    price=models.IntegerField()
    image=models.ImageField(upload_to='images/',null=True)

class User(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    price=models.IntegerField()
    image=models.ImageField(upload_to='images/',null=True)
    

    
    
    
