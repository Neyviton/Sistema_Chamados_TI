
# Importações
from django.shortcuts import render


# Dashboard
def dashboard(request):
    # Dados enviados para o template
    contexto = {
        'titulo': 'Dashboard',
    }

    # Exibe a página principal
    return render(request, 'assistencia/dashboard.html', contexto)


# Lista de clientes
def clientes_lista(request):
    # Lista vazia até a integração com os models
    contexto = {
        'clientes': [],
        'mensagem': 'O cadastro de clientes será disponibilizado após a integração do banco de dados.',
    }

    # Exibe a lista de clientes
    return render(request, 'assistencia/clientes/lista.html', contexto)


# Cadastro de clientes
def cliente_criar(request):
    # Página temporária até a criação dos forms
    contexto = {
        'titulo': 'Cadastrar cliente',
        'mensagem': 'O formulário será conectado após a criação dos models e forms.',
    }

    return render(request, 'assistencia/clientes/formulario.html', contexto)


# Detalhes do cliente
def cliente_detalhes(request, pk):
    # Página temporária até a integração com o banco
    contexto = {
        'mensagem': 'Os detalhes estarão disponíveis após a integração do banco de dados.',
    }

    return render(request, 'assistencia/clientes/detalhes.html', contexto)


# Edição de clientes
def cliente_editar(request, pk):
    # Página temporária até a criação dos forms
    contexto = {
        'titulo': 'Editar cliente',
        'mensagem': 'A edição será disponibilizada após a integração dos models e forms.',
    }

    return render(request, 'assistencia/clientes/formulario.html', contexto)


# Exclusão de clientes
def cliente_excluir(request, pk):
    # Página temporária até a integração com o banco
    contexto = {
        'mensagem': 'A exclusão será disponibilizada após a integração do banco de dados.',
    }

    return render(request, 'assistencia/clientes/detalhes.html', contexto)
<<<<<<< HEAD

# assistencia/views.py

from django.shortcuts import render


# Lista de equipamentos — dados fictícios para visualização
def equipamentos_lista(request):
    equipamentos = [
        {
            'id': 1,
            'cliente': 'João da Silva',
            'tipo': 'Celular',
            'marca': 'Samsung',
            'modelo': 'Galaxy A54',
            'numero_serie': 'SN123456',
        },
        {
            'id': 2,
            'cliente': 'Maria Oliveira',
            'tipo': 'Notebook',
            'marca': 'Dell',
            'modelo': 'Inspiron 15',
            'numero_serie': 'SN789012',
        },
        {
            'id': 3,
            'cliente': 'Pedro Santos',
            'tipo': 'Computador',
            'marca': 'Lenovo',
            'modelo': 'IdeaCentre',
            'numero_serie': 'SN345678',
        },
    ]

    contexto = {
        'equipamentos': equipamentos,
    }

    return render(
        request,
        'assistencia/equipamentos/lista.html',
        contexto,
    )


# Formulário visual de cadastro
def equipamento_criar(request):
    contexto = {
        'titulo': 'Cadastrar equipamento',
        'modo': 'criar',
    }

    return render(
        request,
        'assistencia/equipamentos/formulario.html',
        contexto,
    )


# Detalhes de um equipamento fictício
def equipamento_detalhes(request, pk):
    equipamento = {
        'id': pk,
        'cliente': 'João da Silva',
        'tipo': 'Celular',
        'marca': 'Samsung',
        'modelo': 'Galaxy A54',
        'numero_serie': 'SN123456',
        'descricao': 'Equipamento recebido para avaliação técnica.',
        'data_cadastro': '16/10/2026',
    }

    contexto = {
        'equipamento': equipamento,
    }

    return render(
        request,
        'assistencia/equipamentos/detalhes.html',
        contexto,
    )


# Formulário visual de edição
def equipamento_editar(request, pk):
    contexto = {
        'titulo': 'Editar equipamento',
        'modo': 'editar',
        'equipamento_id': pk,
    }

    return render(
        request,
        'assistencia/equipamentos/formulario.html',
        contexto,
    )

# assistencia/views.py

# Lista visual de Ordens de Serviço
def ordens_servico_lista(request):
    ordens_servico = [
        {
            'id': 1,
            'equipamento': 'Samsung Galaxy A54',
            'cliente': 'João da Silva',
            'tecnico': 'Carlos Mendes',
            'status': 'EM_REPARO',
            'status_label': 'Em reparo',
            'prioridade': 'ALTA',
            'prioridade_label': 'Alta',
            'orcamento': '250,00',
            'data_entrada': '16/10/2026',
        },
        {
            'id': 2,
            'equipamento': 'Dell Inspiron 15',
            'cliente': 'Maria Oliveira',
            'tecnico': 'Ana Costa',
            'status': 'EM_ANALISE',
            'status_label': 'Em análise',
            'prioridade': 'NORMAL',
            'prioridade_label': 'Normal',
            'orcamento': '180,00',
            'data_entrada': '15/10/2026',
        },
        {
            'id': 3,
            'equipamento': 'Lenovo IdeaCentre',
            'cliente': 'Pedro Santos',
            'tecnico': None,
            'status': 'RECEBIDA',
            'status_label': 'Recebida',
            'prioridade': 'URGENTE',
            'prioridade_label': 'Urgente',
            'orcamento': None,
            'data_entrada': '14/10/2026',
        },
    ]

    contexto = {
        'ordens_servico': ordens_servico,
    }

    return render(
        request,
        'assistencia/ordens_servico/lista.html',
        contexto,
    )


# Formulário visual para cadastro de ordem
def ordem_servico_criar(request):
    contexto = {
        'titulo': 'Nova Ordem de Serviço',
        'modo': 'criar',
    }

    return render(
        request,
        'assistencia/ordens_servico/formulario.html',
        contexto,
    )


# Detalhes de uma ordem fictícia
def ordem_servico_detalhes(request, pk):
    ordem = {
        'id': pk,
        'equipamento': 'Samsung Galaxy A54',
        'cliente': 'João da Silva',
        'tecnico': 'Carlos Mendes',
        'descricao_problema': 'Equipamento não está carregando corretamente.',
        'diagnostico': 'Conector de carregamento precisa ser avaliado.',
        'status': 'EM_REPARO',
        'status_label': 'Em reparo',
        'prioridade': 'ALTA',
        'prioridade_label': 'Alta',
        'orcamento': '250,00',
        'orcamento_aprovado': False,
        'data_entrada': '16/10/2026 às 09:30',
        'data_previsao': '20/10/2026 às 17:00',
        'data_saida': None,
    }

    contexto = {
        'ordem': ordem,
    }

    return render(
        request,
        'assistencia/ordens_servico/detalhes.html',
        contexto,
    )


# Formulário visual para edição de ordem
def ordem_servico_editar(request, pk):
    contexto = {
        'titulo': 'Editar Ordem de Serviço',
        'modo': 'editar',
        'ordem_id': pk,
    }

    return render(
        request,
        'assistencia/ordens_servico/formulario.html',
        contexto,
    )
=======
    
>>>>>>> 905054acc3f381effd05f51418fc522fc3ba301a
