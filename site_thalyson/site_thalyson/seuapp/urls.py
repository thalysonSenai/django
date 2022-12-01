from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('cadastro/', views.cadastro, name ='cadastro'),
    path('docad/',views.docad, name='docad'),
    path('dolog/',views.dolog, name="dolog"),
    path('login/', views.login, name='login'),
    path('esqueceuSenha/', views.esqueceuSenha, name='esqueceuSenha'),
    path('novaSenha/', views.novaSenha, name='novaSenha'),
    path('errorLogin/', views.errorLogin, name='errorLogin'),
    path('errorEditar/', views.errorEditar, name='errorEditar'),
    path('historico/', views.historico, name='historico'),
    path('agendErro/', views.agendErro, name='agendErro'),
    path('dologout/', views.dologout, name='dologout'),
    path('logout/', views.logout, name='logout'),
    path('perfil/', views.profile, name='perfil'),
    path('doupdate/', views.doupdate, name='doupdate'),
    path('agendamento/', views.agendamento, name='agendamento'),
    path('agendamento/<int:id>/editar',views.edit_agend, name='edit_agend'),
    path('agend_delete/<int:id>/deletar',views.agend_delete, name='agend_delete'),
]