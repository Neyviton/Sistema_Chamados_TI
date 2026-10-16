
# Importações
from django.urls import path
from . import views


# Nome do aplicativo
app_name = 'assistencia'


# Rotas do sistema
urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Clientes
    path('clientes/', views.clientes_lista, name='clientes_lista'),
    path('clientes/novo/', views.cliente_criar, name='cliente_criar'),
    path('clientes/<int:pk>/', views.cliente_detalhes, name='cliente_detalhes'),
    path('clientes/<int:pk>/editar/', views.cliente_editar, name='cliente_editar'),
    path('clientes/<int:pk>/excluir/', views.cliente_excluir, name='cliente_excluir'),

     # Equipamentos
    path(
        'equipamentos/',
        views.equipamentos_lista,
        name='equipamentos_lista',
    ),
    path(
        'equipamentos/novo/',
        views.equipamento_criar,
        name='equipamento_criar',
    ),
    path(
        'equipamentos/<int:pk>/',
        views.equipamento_detalhes,
        name='equipamento_detalhes',
    ),
    path(
        'equipamentos/<int:pk>/editar/',
        views.equipamento_editar,
        name='equipamento_editar',
    ),
]
