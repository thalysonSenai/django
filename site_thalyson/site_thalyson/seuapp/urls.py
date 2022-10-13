from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name ='cadastro'),
    path('docad/',views.docad, name='docad'),
    path('docade/',views.docade, name="docade"),
    path('login/', views.login, name='login'),
    path('esqueceuSenha/', views.esqueceuSenha, name='esqueceuSenha'),
    path('novaSenha/', views.novaSenha, name='novaSenha')
]