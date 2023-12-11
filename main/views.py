from django.shortcuts import render, redirect
from .forms import BrokerForm, ClientForm, RegisterForm, PostForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from .models import Broker, Client, Post


@login_required(login_url="/login")
def home(request):
    posts = Post.objects.all()

    return render(request, 'main/home.html', {"posts": posts})


# Broker views
@login_required(login_url="/login")
def brokers(request):
    print(request.method)
    brokers = Broker.objects.all()
    if request.method ==  "POST":
        broker_id = request.POST.get("broker_id")
        get_client_broker_id = request.POST.get("get_client_broker_id")
        if broker_id:
            broker = Broker.objects.get(id=broker_id)
            broker.delete()
            return render(request, 'main/brokers.html',  {"brokers": brokers})
        if get_client_broker_id:
            broker = Broker.objects.get(id=get_client_broker_id)
            clients = Client.objects.filter(broker=broker)
            return redirect("/clients")
        return redirect("/create_broker")
    return render(request, 'main/brokers.html',  {"brokers": brokers})

def create_broker(request):
    if request.method == 'POST':
        form = BrokerForm(request.POST)
        if form.is_valid():
            broker = form.save(commit=False)
            broker.save()
            brokers = Broker.objects.all()
            return render(request, 'main/brokers.html',  {"brokers": brokers})
    else:
        form = BrokerForm()

    return render(request, 'main/add_broker.html', {"form": form})

#client views
@login_required(login_url="/login")
def clients(request):
    clients = Client.objects.all()
    if request.method ==  "POST":
        client_id = request.POST.get("client_id")
        if client_id:
            client = Client.objects.get(id=client_id)
            client.delete()
            return render(request, 'main/clients.html',  {"clients": clients})
        return redirect("/create_client")
    return render(request, 'main/clients.html', {"clients": clients})

def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.save()
            clients = Client.objects.all()
            return render(request, 'main/clients.html',  {"clients": clients})
    else:
        form = ClientForm()      
    return render(request, 'main/add_client.html', {"form": form})


#Authentication views
def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})



