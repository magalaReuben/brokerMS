from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Broker, Client, Titles, Agent


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description"]
        
class BrokerForm(forms.ModelForm):
    class Meta:
        model = Broker
        fields = ["name", "number"]
        
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        Amount_paid_by = forms.DateTimeField(widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM:SS'}))
        fields = ["broker", "name", "phone", "locaton", "Amount_paid", "commision", "commision_paid"]
    
class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ["name", "phone"]
        
class TitleForm(forms.ModelForm):
    class Meta:
        model = Titles
        fields = ["name", "agent", "file", "block", "price", "price_paid", "location", "plot", "reason"]
