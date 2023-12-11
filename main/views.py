from django.shortcuts import render, redirect
from .forms import AgentForm, BrokerForm, ClientForm, RegisterForm, PostForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from .models import Agent, Broker, Client, Post


@login_required(login_url="/login")
def home(request):
    print("home")
    posts = Post.objects.all()
    return render(request, 'main/home.html', {"posts": posts})


# Broker views
@login_required(login_url="/login")
def brokers(request):
    print("brokers")
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
            return redirect(f"/clients/{get_client_broker_id}")
        return redirect("/create_broker")
    return render(request, 'main/brokers.html',  {"brokers": brokers})

def create_broker(request):
    print("create_broker")
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
def clients(request, pk):
    print("clients")
    client_id = request.POST.get("client_id")
    clients = Client.objects.all()
    selected_clients = []
    for client in clients:
        if client.broker.id == pk:
            selected_clients.append(client)
    if request.method ==  "POST":
        client_id = request.POST.get("client_id")
        if client_id:
            client = Client.objects.get(id=client_id)
            print(client)
            return render(request, 'main/client_details.html',  {"client": client})
        return redirect("/create_client")
    return render(request, 'main/clients.html', {"clients":selected_clients})

def create_client(request):
    print("create_client")
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

#Title Views
def titles(request):
    print("titles")
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.save(commit=False)
            title.author = request.user
            title.save()
            return redirect('/home')
    return render(request, 'main/titles.html')

#agents
@login_required(login_url="/login")
def agents(request):
    print("agents")
    agents = Agent.objects.all()
    selected_agents = []
    print(agents)
    if request.method == 'POST':
        agent_id = request.POST.get("agent_id")
        if agent_id:
            agent = Agent.objects.get(id=agent_id)
            agent.delete()
        return render(request, 'main/brokers.html',  {"brokers": brokers})
        return redirect('/create_agent')
    return render(request, 'main/agent.html',  {"agents": agents})

def create_agent(request):
    print("create_agent")
    if request.method == 'POST':
        print("This is it")
        form = AgentForm(request.POST)
        if form.is_valid():
            agent = form.save(commit=False)
            agent.save()
            agents = Agent.objects.all()
            return render(request, 'main/agent.html',  {"agents": agents})
    else:
        form = AgentForm()
    return render(request, 'main/add_agent.html', {"form": form})

#Authentication views
def sign_up(request):
    print("sign_up")
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})



