from django.shortcuts import render, redirect

from main.utils import render_to_pdf
from .forms import AgentForm, BrokerForm, ClientForm, RegisterForm, PostForm, TitleForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from django.db.models import Q
from .models import Agent, Broker, Client, Post, TitleTransactions, Titles, Transaction

@login_required(login_url="/login")
def print_pdf(request, pk):
    template_name = "main/client_transactions.html"
    client = Client.objects.get(id=pk)
    transactions = Transaction.objects.filter(client=client)
    return render_to_pdf(
        template_name,
        {
            "transactions": transactions, "client": client
        }
        )
    

@login_required(login_url="/login")
def home(request):
    print("home")
    posts = Post.objects.all()
    return render(request, 'main/home.html', {"posts": posts})

def documents(request):
    title_id = request.POST.get("title_id")
    print_value = request.POST.get("print_value")
    if title_id:
        title = Titles.objects.get(id=title_id)
        balance = title.price - title.price_paid
        transactions = TitleTransactions.objects.filter(title=title)
    return render(request, 'main/documents.html', {"title": title, "balance": balance, "transactions": transactions})

@login_required(login_url="/login")
def document_payment(request):
    title_id = request.POST.get("title_id")
    amount_paid = request.POST.get("payment")
    if amount_paid != "":
        title = Titles.objects.get(id=title_id)
        title.price_paid = (int(amount_paid) + int(title.price_paid))
        title.save() 
        balance = title.price - title.price_paid
        transaction = TitleTransactions.objects.create(title=title, amount=amount_paid, balance=balance)
        transaction.save()
        transactions = TitleTransactions.objects.filter(title=title)
    title = Titles.objects.get(id=title_id)
    balance = title.price - title.price_paid
    return render(request, 'main/documents.html', {"title": title, "balance": balance, "transactions": transactions})

@login_required(login_url="/login")
def index(request):
    search_client = request.GET.get('search')
    print(search_client)
    if search_client:
        client = Client.objects.filter(Q(name__icontains=search_client))
        print(len(client))
        if len(client) == 0:
            return render(request, 'main/clients.html', {"clients": []})
        else:
            return render(request, 'main/clients.html', {"clients": client})
    else:
        brokers = Broker.objects.all()
        return render(request, 'main/brokers.html',  {"brokers": brokers})
    
@login_required(login_url="/login")
def payment(request):
    client_id = request.POST.get("client_id")
    amount_paid = request.POST.get("payment")
    if amount_paid != "":
        client = Client.objects.get(id=client_id)
        client.commision_paid = (int(amount_paid) + int(client.commision_paid))
        client.save() 
        balance = client.commision - client.commision_paid
        transaction = Transaction.objects.create(client=client, amount=amount_paid, balance=balance)
        transaction.save()
        transactions = Transaction.objects.filter(client=client)
    client = Client.objects.get(id=client_id)
    balance = client.commision - client.commision_paid
    return render(request, 'main/client_details.html',  {"client": client, "balance": balance, "transactions": transactions})
    


# Broker views
@login_required(login_url="/login")
def brokers(request):
    brokers = Broker.objects.all()
    broker_balance_dict = {}
    for broker in brokers:
        clients = Client.objects.filter(broker=broker)
        balance = sum((client.commision - client.commision_paid) for client in clients)
        broker_balance_dict[broker] = balance
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
    return render(request, 'main/brokers.html',  {"brokers": brokers, "broker_balance_dict": broker_balance_dict})

def create_broker(request):
    print("create_broker")
    if request.method == 'POST':
        form = BrokerForm(request.POST)
        if form.is_valid():
            broker = form.save(commit=False)
            broker.save()
            brokers = Broker.objects.all()
            return redirect('/brokers',  {"brokers": brokers})
    else:
        form = BrokerForm()

    return render(request, 'main/add_broker.html', {"form": form})

#client views
@login_required(login_url="/login")
def clients(request, pk):
    client_id = request.POST.get("client_id")
    clients = Client.objects.all()
    selected_clients = []
    for client in clients:
        if client.broker.id == pk:
            selected_clients.append(client)
    if request.method ==  "POST":
        client_id = request.POST.get("client_id")
        value_id = request.POST.get("print_value")
        if client_id:
            client = Client.objects.get(id=client_id)
            balance = client.commision - client.commision_paid
            transactions = Transaction.objects.filter(client=client)
            return render(request, 'main/client_details.html',  {"client": client, "balance": balance, "transactions": transactions})
        if value_id:
            return redirect(f'/print/{value_id}')
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
            selected_clients = []
            for client in clients:
                if client.broker.id == form.data['broker']:
                    selected_clients.append(client)
            balance = client.commision - client.commision_paid
            transaction = Transaction.objects.create(client=client, amount=form.data['Amount_paid'], balance=balance)
            transaction.save()
            return redirect('/clients/'+str(form.data['broker']),  {"clients": selected_clients})
    else:
        form = ClientForm()      
    return render(request, 'main/add_client.html', {"form": form})

#Title Views
def titles(request, pk):
    print("titles")
    titles = Titles.objects.all()
    selected_titles = []
    for title in titles:
        if title.agent.id == pk:
            selected_titles.append(title)
    if request.method == 'POST':
        title_id = request.POST.get("title_id")
        if title_id:
            title = Titles.objects.get(id=title_id)
            title.delete()
            return render(request, 'main/titles.html',  {"titles": titles})
        return redirect('/create_title')    
    return render(request, 'main/titles.html', {"titles": selected_titles})

def create_title(request):
    print("create_title")
    if request.method == 'POST':
        form = TitleForm(request.POST,request.FILES)
        if form.is_valid():
            title = form.save(commit=False)
            title.save()
            titles = Titles.objects.all()
            balance = title.price - title.price_paid
            transaction = TitleTransactions(title=title, amount=title.price_paid, balance=balance)
            transaction.save()
            return redirect('/titles/'+str(form.data['agent']),  {"titles": titles})
    else:
        form = TitleForm()
    return render(request, 'main/add_title.html', {"form": form})

#agents
@login_required(login_url="/login")
def agents(request):
    print("agents")
    agents = Agent.objects.all()
    selected_agents = []
    print(agents)
    if request.method == 'POST':
        agent_id = request.POST.get("agent_id")
        get_agent_id = request.POST.get("get_agent_id")
        if agent_id:
            agent = Agent.objects.get(id=agent_id)
            agent.delete()
            return render(request, 'main/agent.html',  {"agents": agents})
        if get_agent_id:
            agent = Agent.objects.get(id=get_agent_id)
            return redirect(f"/titles/{get_agent_id}")
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
            return redirect('/agents', {"agents": agents})
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



