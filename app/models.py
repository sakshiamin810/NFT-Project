from distutils.command.upload import upload
from email.policy import default
from django.db import models


# Create your models here.

class User(models.Model):
    image = models.ImageField(upload_to="img/",default="abc.jpg")
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=150)

class category(models.Model):
    categoryname = models.CharField(max_length=150)
    def __str__(self) -> str:
        return self.categoryname
    
class product(models.Model):
    cat_id = models.ForeignKey(category,on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=150)
    price = models.CharField(max_length=150)
    creator = models.CharField(max_length=150)
    minimumbid = models.CharField(max_length=150)
    bid = models.CharField(max_length=150)
    history = models.CharField(max_length=150)
    details = models.CharField(max_length=150)
    image1 = models.ImageField(upload_to="app/img",default="abc.jpg")
    image2 = models.ImageField(upload_to="app/img",default="abc.jpg")
    image3 = models.ImageField(upload_to="app/img",default="abc.jpg")
    image4 = models.ImageField(upload_to="app/img",default="abc.jpg")

    def __str__(self) -> str:
        return self.name

     
