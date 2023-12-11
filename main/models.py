from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + "\n" + self.description
    
    

class Client(models.Model):
    broker = models.ForeignKey('Broker', on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    locaton = models.CharField(max_length=45)
    Amount_paid_by = models.DateTimeField()
    commision_paid = models.IntegerField()
    balance = models.IntegerField()
    signature = models.FileField(upload_to='uploads/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name
    
class Broker(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name
    
class Agent(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name
    
class Titles(models.Model):
    file = models.FileField(upload_to='files/uploads/', null=True)
    block = models.CharField(max_length=45)
    location = models.CharField(max_length=45)
    plot = models.CharField(max_length=45)
    reason = models.CharField(max_length=45)
    signature = models.FileField(upload_to='files/uploads/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.block + "\n" + self.location + "\n" + self.plot + "\n" + self.reason
    
    
    
    