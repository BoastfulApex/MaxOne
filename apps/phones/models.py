from django.db import models


class Category(models.Model):
    name_uz = models.CharField(max_length=100, null=True, blank=True)
    name_ru = models.CharField(max_length=100, null=True, blank=True)
    name_en = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    
    @property
    def PhotoURL(self):
        try:
            return self.image.url
        except:
            return ''
    
    def __str__(self):
        return self.name_uz      


class Brand(models.Model):
    name_uz = models.CharField(max_length=100, null=True, blank=True)
    name_ru = models.CharField(max_length=100, null=True, blank=True)
    name_en = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    @property
    def PhotoURL(self):
        try:
            return self.image.url
        except:
            return ''    

    def __str__(self):
        return self.name_uz      


class Type(models.Model):
    name_uz = models.CharField(max_length=100, null=True, blank=True)
    name_ru = models.CharField(max_length=100, null=True, blank=True)
    name_en = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    @property
    def PhotoURL(self):
        try:
            return self.image.url
        except:
            return ''    

    def __str__(self):
        return self.name_uz      
    

class Product(models.Model):
    name_uz = models.CharField(max_length=100, null=True, blank=True)
    name_ru = models.CharField(max_length=100, null=True, blank=True)
    name_en = models.CharField(max_length=100, null=True, blank=True)
    description_uz = models.CharField(max_length=100, null=True, blank=True)
    description_ru = models.CharField(max_length=100, null=True, blank=True)
    description_en = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL,  null=True, blank=True)
    price = models.IntegerField()
    characteristic_uz = models.TextField(max_length=1000, null=True, blank=True)
    characteristic_ru = models.TextField(max_length=1000, null=True, blank=True)
    characteristic_en = models.TextField(max_length=1000, null=True, blank=True)
    best = models.BooleanField(default = False)
    orders = models.IntegerField(default=0)
    this_week_orders = models.IntegerField(default=0)
    last_week_orders = models.IntegerField(default=0)

    def __str__(self):
        return self.name_uz      
    

class Color(models.Model):
    color_en = models.CharField(max_length=50, null=True, blank=True)
    color_uz = models.CharField(max_length=50, null=True, blank=True)
    color_ru = models.CharField(max_length=50, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True)

    # def __str__(self):
    #     return f"{self.color_en}"      

    @property
    def Photo1URL(self):
        try:
            return self.image1.url
        except:
            return ''


class Slider(models.Model):
    name_uz = models.CharField(max_length=100, null=True, blank=True)
    name_ru = models.CharField(max_length=100, null=True, blank=True)
    name_en = models.CharField(max_length=100, null=True, blank=True)
    description_uz = models.CharField(max_length=100, null=True, blank=True)
    description_ru = models.CharField(max_length=100, null=True, blank=True)
    description_en = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    @property
    def PhotoURL(self):
        try:
            return self.image.url
        except:
            return ''  
        

class Lead(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    customer_name = models.CharField(max_length=200, null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    product_name = models.CharField(max_length=500, null=True, blank=True)
    price = models.IntegerField(default=0)


class Visit(models.Model):
    date = models.DateField()
    count = models.IntegerField(default=0)