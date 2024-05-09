from django.db import models
from authentication.models import Profile

class UniDetail(models.Model):
    uni = models.OneToOneField(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uni/images/')
    description = models.TextField()
    
    class Meta:
        verbose_name_plural = 'University Details'
        
    def __str__(self):
        return self.name
    

class UniCourse(models.Model):
    uni = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uni/images/')
    length = models.CharField(max_length=50)
    fees = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class UniService(models.Model):
    uni = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class UniContactInfo(models.Model):
    uni = models.OneToOneField(Profile, on_delete=models.CASCADE)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)
    post_code = models.CharField(max_length=10)
    location = models.TextField()

    def __str__(self):
        return self.uni.user.email
    
class UniUserQuery(models.Model):
    uni = models.ForeignKey(Profile, on_delete=models.CASCADE)
    email = models.EmailField()
    fullname = models.CharField(max_length=50)
    message = models.TextField()
    
    def __str__(self):
        return self.email


