from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('brokers', views.brokers, name='brokers'),
    path('clients/<int:pk>', views.clients, name='clients'),
    path('titles/<int:pk>', views.titles, name='titles'),
    path('agents', views.agents, name='agents'),
    path('create_agent', views.create_agent, name='create_agent'),
    path('create_broker', views.create_broker, name='create_broker'),
    path('create_client', views.create_client, name='create_client'),
    path('create_title', views.create_title, name='create_title'),
    path('index', views.index, name='index'),
    path('payment', views.payment, name='payment'),
    path('sign-up', views.sign_up, name='sign_up'),
]
