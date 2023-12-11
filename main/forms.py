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
        fields = ["name"]
        
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        Amount_paid_by = forms.DateTimeField(widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM:SS'}))
        fields = ["broker", "name", "locaton", "Amount_paid_by", "commision_paid", "balance"]
    
class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ["name"]
        
class TitleForm(forms.ModelForm):
    class Meta:
        model = Titles
        fields = ["agent", "file", "block", "location", "plot", "reason", "signature"]
