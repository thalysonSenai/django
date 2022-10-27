from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('cadastro/', views.cadastro, name ='cadastro'),
    path('docad/',views.docad, name='docad'),
    path('dolog/',views.dolog, name="dolog"),
    path('login/', views.login, name='login'),
    path('esqueceuSenha/', views.esqueceuSenha, name='esqueceuSenha'),
    path('novaSenha/', views.novaSenha, name='novaSenha'),
    path('errorLogin/', views.errorLogin, name='errorLogin'),
    path('errorEditar/', views.errorEditar, name='errorEditar'),
    path('dologout/', views.dologout, name='dologout'),
    path('logout/', views.logout, name='logout'),
    path('perfil/', views.profile, name='perfil'),
    path('doupdate/', views.doupdate, name='doupdate'),
]