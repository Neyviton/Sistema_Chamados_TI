
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

    # Rotas de Ordens de Serviço
path(
    'ordens-servico/',
    views.ordens_servico_lista,
    name='ordens_servico_lista',
),
path(
    'ordens-servico/nova/',
    views.ordem_servico_criar,
    name='ordem_servico_criar',
),
path(
    'ordens-servico/<int:pk>/',
    views.ordem_servico_detalhes,
    name='ordem_servico_detalhes',
),
path(
    'ordens-servico/<int:pk>/editar/',
    views.ordem_servico_editar,
    name='ordem_servico_editar',
),

# Rotas de Pagamentos
path(
    'pagamentos/',
    views.pagamentos_lista,
    name='pagamentos_lista',
),
path(
    'pagamentos/novo/',
    views.pagamento_criar,
    name='pagamento_criar',
),
path(
    'pagamentos/<int:pk>/',
    views.pagamento_detalhes,
    name='pagamento_detalhes',
),
path(
    'pagamentos/<int:pk>/editar/',
    views.pagamento_editar,
    name='pagamento_editar',
),

# Rotas da área de técnicos
path(
    'tecnicos/',
    views.tecnicos_lista,
    name='tecnicos_lista'
),

path(
    'tecnicos/novo/',
    views.tecnico_criar,
    name='tecnico_criar'
),

path(
    'tecnicos/<int:pk>/',
    views.tecnico_detalhes,
    name='tecnico_detalhes'
),

path(
    'tecnicos/<int:pk>/editar/',
    views.tecnico_editar,
    name='tecnico_editar'
),
]

