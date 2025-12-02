from django.db import models

class Category_model(models.Model):
    name=models.CharField(("category name"), max_length=50)
    image=models.ImageField(("upload image"), upload_to='images', height_field=None, width_field=None, max_length=None)
    descriptions=models.TextField(("description"))
    
    def __str__(self):
      return self.name
    

class Product_model(models.Model):
    name=models.CharField(("product name"), max_length=50)
    image=models.ImageField(("upload image"), upload_to='images', height_field=None, width_field=None, max_length=None)
    descriptions=models.TextField(("description"))
    price=models.FloatField(("price"))
    stock=models.IntegerField(("stock"))
    available=models.BooleanField(("available"),default=True)
    created=models.DateTimeField(("created"),auto_now_add=True)
    updated=models.DateTimeField(("updated"),auto_now_add=True)
    category=models.ForeignKey(Category_model,on_delete=models.CASCADE,related_name='category')
    
    def __str__(self):
      return self.name

