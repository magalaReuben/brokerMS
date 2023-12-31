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
    Amount_paid = models.IntegerField()
    phone = models.CharField(max_length=45)
    commision = models.IntegerField()
    commision_paid = models.IntegerField()
    signature = models.FileField(upload_to='uploads/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name
    
class Transaction(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    balance = models.IntegerField()
    
class Broker(models.Model):
    name = models.CharField(max_length=45)
    number = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name
    
class Agent(models.Model):
    name = models.CharField(max_length=45)
    phone = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name
    
class Titles(models.Model):
    agent = models.ForeignKey('Agent', on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    file = models.FileField(upload_to='files/uploads/', null=True)
    block = models.CharField(max_length=45)
    location = models.CharField(max_length=45)
    plot = models.CharField(max_length=45)
    reason = models.CharField(max_length=45)
    price = models.IntegerField()
    price_paid = models.IntegerField()
    reason = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.block + "\n" + self.location + "\n" + self.plot + "\n" + self.reason
    
class TitleTransactions(models.Model):
    title = models.ForeignKey('Titles', on_delete=models.CASCADE)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    balance = models.IntegerField()
    
    
    
    