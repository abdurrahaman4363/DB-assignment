from django.db import models

class ProductCategory(models.Model):
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=100)  
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 
    modified_at = models.DateTimeField(auto_now=True)  
    deleted_at = models.DateTimeField(null=True, blank=True) 

    def __str__(self):
        return self.name
    
class ProductInventory(models.Model):
    id = models.AutoField(primary_key=True)  
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True) 
    modified_at = models.DateTimeField(auto_now=True)  
    deleted_at = models.DateTimeField(null=True, blank=True) 

    def __str__(self):
        return str(self.quantity)  
    
class Discount(models.Model):
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=100)
    desc = models.TextField()
    discount_percent = models.DecimalField(max_digits=10,decimal_places=2)  
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True) 
    modified_at = models.DateTimeField(auto_now=True) 
    deleted_at = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    desc = models.TextField()
    sku = models.CharField(max_length=100) 
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name="category")
    inventory = models.OneToOneField(ProductInventory, on_delete=models.CASCADE, related_name='inventory')
    price = models.DecimalField(max_digits=10,decimal_places=2) 
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, related_name="discount")
    created_at = models.DateTimeField(auto_now_add=True) 
    modified_at = models.DateTimeField(auto_now=True) 
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.name
