from django.contrib import admin
from .models import Agent, Broker, Client, Post, Titles, Transaction

# Register your models here.
admin.site.register(Post)
admin.site.register(Broker)
admin.site.register(Client)
admin.site.register(Agent)
admin.site.register(Titles)
admin.site.register(Transaction)
