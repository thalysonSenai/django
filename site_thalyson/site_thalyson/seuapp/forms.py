from cgitb import text
from faulthandler import disable
from multiprocessing.resource_sharer import stop
from django.forms import ModelForm
from django import forms
from seuapp.models import Usuario, Agendamento

# Create the form class.
class UsersForm(ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    confirma_senha = forms.CharField(widget=forms.PasswordInput)
    confirma_nova_senha = forms.CharField(widget=forms.PasswordInput)
    nascimento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    tel = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Digite seu número de telefone', 'onkeypress': 'formatNumber(event)', 'maxlength': '15', 'required' : 'True'}))
    class Meta:
        model = Usuario
        widgets = {'password': forms.PasswordInput(),}
        fields = ['usuario', 'email', 'senha', 'confirma_senha','confirma_nova_senha','tel', 'nascimento']

class LoginForm(ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Usuario
        widgets = {'password': forms.PasswordInput(),}
        fields = ['usuario', 'senha']


class AgendamentoForm(ModelForm):
    data = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    hora = forms.TimeField(widget= forms.TimeInput(attrs={'type': 'time'}))
    class Meta:
        model = Agendamento
        fields = ['nome', 'sobrenome', 'celular', 'data', 'hora']       







