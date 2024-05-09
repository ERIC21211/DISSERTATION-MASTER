from django.db import models
from authentication.models import CustomUser

class Company(models.Model):
    image = models.ImageField(upload_to='company/images/')
    description = models.TextField()
    
    def __str__(self):
        return self.description
    
class History(models.Model):
    image = models.ImageField(upload_to='history/images/')
    description = models.TextField()
    
    def __str__(self):
        return self.description
    
class Mission(models.Model):
    description = models.TextField()
    
    def __str__(self):
        return self.description
    
class CEO(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='ceo/images/')
    description = models.TextField()
    
    def __str__(self):
        return self.description
    
class Product(models.Model):
    description = models.TextField()
    
    def __str__(self):
        return self.description
    
class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    
    def __str__(self):
        return self.name
    

class UserPost(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    post_likes = models.ManyToManyField(CustomUser, related_name='likes', blank=True)
    
    def __str__(self):
        return self.content