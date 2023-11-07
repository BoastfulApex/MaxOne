from django.db import models


class Slider(models.Model):
    name_uz = models.CharField(max_length=100, null=True, blank=True)
    name_en = models.CharField(max_length=100, null=True, blank=True)
    name_ru = models.CharField(max_length=100, null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)
    tag_uz = models.CharField(max_length=100, null=True, blank=True)
    tag_en = models.CharField(max_length=100, null=True, blank=True)
    tag_ru = models.CharField(max_length=100, null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    @property
    def PhotoURL(self):
        try:
            return self.photo.url
        except:
            return ''    


class Service(models.Model):
    name_uz = models.CharField(max_length=100, null=True, blank=True)
    name_en = models.CharField(max_length=100, null=True, blank=True)
    name_ru = models.CharField(max_length=100, null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)
    text_uz = models.TextField(max_length=500, null=True, blank=True)
    text_en = models.TextField(max_length=500, null=True, blank=True)
    text_ru = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name_uz
    

class Article(models.Model):
    name_uz = models.CharField(max_length=100, null=True, blank=True)
    name_en = models.CharField(max_length=100, null=True, blank=True)
    name_ru = models.CharField(max_length=100, null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)
    text_uz = models.TextField(max_length=500, null=True, blank=True)
    text_en = models.TextField(max_length=500, null=True, blank=True)
    text_ru = models.TextField(max_length=500, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name_uz
    


class Pertner(models.Model):
    photo = models.ImageField(null=True, blank=True)
    

class Reklama(models.Model):
    name_uz = models.CharField(max_length=100, null=True, blank=True)
    name_en = models.CharField(max_length=100, null=True, blank=True)
    name_ru = models.CharField(max_length=100, null=True, blank=True)
    description_uz = models.TextField(max_length=500, null=True, blank=True)
    description_en = models.TextField(max_length=500, null=True, blank=True)
    description_ru = models.TextField(max_length=500, null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name_uz


class Type(models.Model):
    name_uz = models.CharField(max_length=100, null=True, blank=True)
    name_en = models.CharField(max_length=100, null=True, blank=True)
    name_ru = models.CharField(max_length=100, null=True, blank=True)
    description_uz = models.TextField(max_length=500, null=True, blank=True)
    description_en = models.TextField(max_length=500, null=True, blank=True)
    description_ru = models.TextField(max_length=500, null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name_uz
    

class ServiceSlider(models.Model):
    name_uz = models.CharField(max_length=100, null=True, blank=True)
    name_en = models.CharField(max_length=100, null=True, blank=True)
    name_ru = models.CharField(max_length=100, null=True, blank=True)
    description_uz = models.TextField(max_length=500, null=True, blank=True)
    description_en = models.TextField(max_length=500, null=True, blank=True)
    description_ru = models.TextField(max_length=500, null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name_uz
    

class Team(models.Model):
    photo = models.ImageField(null=True, blank=True)
