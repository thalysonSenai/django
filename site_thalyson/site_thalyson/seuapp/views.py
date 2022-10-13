import email
from django.shortcuts import render, redirect
from seuapp.forms import UsersForm, LoginForm
from seuapp.models import Usuario


# Create your views here.


def home(request):
	tabela = Usuario.objects.all()
	return render(request,'home.html', {'usuario':tabela})

def cadastro(request):
	data = {}
	data['form'] = UsersForm()
	return render(request,'cadastro.html',data)

def login(request):
	data = {}
	data['login'] = LoginForm()
	return render(request,'login.html',data)

def esqueceuSenha(request):
	data = {}
	data['esqueceuSenha'] = UsersForm()
	return render(request,'esqueceuSenha.html',data)

def novaSenha(request):
	data = {}
	data['novaSenha'] = UsersForm()
	return render(request,'novaSenha.html',data)	

def docad(request):
	data = {}
	tabela = Usuario.objects.all()
	form = UsersForm(request.POST or None)
	erro = ''
	for c in tabela:
		if form['usuario'].data == c.usuario :
			erro = "mensagem de erro"
			return render(request,'userError.html', data)
	if form.is_valid() and erro == '':
		form.save()
	return render(request,'registerSucces.html', data)


def docade(request):
	data = {}
	tabela = Usuario.objects.all()
	form = LoginForm(request.POST or None)
	erro = ''
	for c in tabela:
		if form['usuario'].data == c.usuario and form['senha'].data == c.senha:
			return redirect('home')	




