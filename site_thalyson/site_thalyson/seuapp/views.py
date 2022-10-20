import email
from http.client import HTTPResponse

from django.shortcuts import render, redirect
from seuapp.forms import UsersForm, LoginForm
from seuapp.models import Usuario


# Create your views here.


def home(request):
	try:
		profile = {}
		profile['uid'] = Usuario.objects.get(id=request.session['uid'])
		print(profile)
	except:
		return render(request,'home.html')
	return render(request,'home.html', profile)

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

def errorLogin(request):
	data = {}
	return render(request,'errorLogin.html',data)

def docad(request):
	data = {}
	tabela = Usuario.objects.all()
	form = UsersForm(request.POST or None)
	erro = ''
	for c in tabela:
		if form['usuario'].data == c.usuario :
			return render(request,'userError.html', data)
	for c in tabela:
		if form['email'].data == c.email :
			return render(request,'userError.html', data)
	for c in tabela:
		if form['tel'].data == c.tel:
			return render(request,'userError.html', data)
	if form.is_valid() and erro == '':
		form.save()
	return render(request,'registerSucces.html', data)


def dolog(request):
	if request.method == "POST":
		try:
			u = Usuario.objects.get(usuario=request.POST['usuario'])
		except:
			return redirect("errorLogin")
		print(u.usuario)
		if u.senha == request.POST['senha']:
			request.session['uid'] = u.id
			return redirect('home')
		else:
			return redirect("errorLogin")
	else: 
		return redirect ('login')
	






