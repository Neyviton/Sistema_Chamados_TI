
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

# assistencia/views.py

# Lista visual de pagamentos
def pagamentos_lista(request):
    pagamentos = [
        {
            'id': 1,
            'ordem_id': 1,
            'equipamento': 'Samsung Galaxy A54',
            'cliente': 'João da Silva',
            'valor': '250,00',
            'forma_pagamento': 'PIX',
            'forma_label': 'Pix',
            'data_pagamento': '16/10/2026',
        },
        {
            'id': 2,
            'ordem_id': 2,
            'equipamento': 'Dell Inspiron 15',
            'cliente': 'Maria Oliveira',
            'valor': '180,00',
            'forma_pagamento': 'CREDITO',
            'forma_label': 'Cartão de crédito',
            'data_pagamento': '15/10/2026',
        },
        {
            'id': 3,
            'ordem_id': 1,
            'equipamento': 'Samsung Galaxy A54',
            'cliente': 'João da Silva',
            'valor': '100,00',
            'forma_pagamento': 'DINHEIRO',
            'forma_label': 'Dinheiro',
            'data_pagamento': '14/10/2026',
        },
    ]

    contexto = {
        'pagamentos': pagamentos,
    }

    return render(
        request,
        'assistencia/pagamentos/lista.html',
        contexto,
    )


# Formulário visual de cadastro
def pagamento_criar(request):
    contexto = {
        'titulo': 'Registrar pagamento',
        'modo': 'criar',
    }

    return render(
        request,
        'assistencia/pagamentos/formulario.html',
        contexto,
    )


# Detalhes de um pagamento fictício
def pagamento_detalhes(request, pk):
    pagamento = {
        'id': pk,
        'ordem_id': 1,
        'equipamento': 'Samsung Galaxy A54',
        'cliente': 'João da Silva',
        'valor': '250,00',
        'forma_pagamento': 'PIX',
        'forma_label': 'Pix',
        'data_pagamento': '16/10/2026 às 10:30',
        'observacao': 'Pagamento de demonstração.',
    }

    contexto = {
        'pagamento': pagamento,
    }

    return render(
        request,
        'assistencia/pagamentos/detalhes.html',
        contexto,
    )


# Formulário visual de edição
def pagamento_editar(request, pk):
    contexto = {
        'titulo': 'Editar pagamento',
        'modo': 'editar',
        'pagamento_id': pk,
    }

    return render(
        request,
        'assistencia/pagamentos/formulario.html',
        contexto,
    )

# Lista de técnicos
def tecnicos_lista(request):
    tecnicos = [
        {
            'id': 1,
            'nome': 'Carlos Mendes',
            'email': 'carlos@exemplo.com',
            'telefone': '(86) 99999-1111',
            'especialidade': 'Celulares',
            'ativo': True,
        },
        {
            'id': 2,
            'nome': 'Ana Costa',
            'email': 'ana@exemplo.com',
            'telefone': '(86) 99999-2222',
            'especialidade': 'Notebooks',
            'ativo': True,
        },
        {
            'id': 3,
            'nome': 'Roberto Lima',
            'email': 'roberto@exemplo.com',
            'telefone': '(86) 99999-3333',
            'especialidade': 'Computadores',
            'ativo': False,
        },
    ]

    return render(
        request,
        'assistencia/tecnicos/lista.html',
        {'tecnicos': tecnicos}
    )


# Página de cadastro de técnico
def tecnico_criar(request):
    return render(
        request,
        'assistencia/tecnicos/formulario.html',
        {
            'titulo': 'Cadastrar técnico',
            'modo': 'criar',
        }
    )


# Detalhes de um técnico
def tecnico_detalhes(request, pk):
    tecnicos = {
        1: {
            'id': 1,
            'nome': 'Carlos Mendes',
            'email': 'carlos@exemplo.com',
            'telefone': '(86) 99999-1111',
            'especialidade': 'Celulares',
            'ativo': True,
        },
        2: {
            'id': 2,
            'nome': 'Ana Costa',
            'email': 'ana@exemplo.com',
            'telefone': '(86) 99999-2222',
            'especialidade': 'Notebooks',
            'ativo': True,
        },
        3: {
            'id': 3,
            'nome': 'Roberto Lima',
            'email': 'roberto@exemplo.com',
            'telefone': '(86) 99999-3333',
            'especialidade': 'Computadores',
            'ativo': False,
        },
    }

    tecnico = tecnicos.get(pk)

    if tecnico is None:
        return render(
            request,
            'assistencia/tecnicos/detalhes.html',
            {'tecnico': None}
        )

    return render(
        request,
        'assistencia/tecnicos/detalhes.html',
        {'tecnico': tecnico}
    )


# Página de edição de técnico
def tecnico_editar(request, pk):
    tecnicos = {
        1: 'Carlos Mendes',
        2: 'Ana Costa',
        3: 'Roberto Lima',
    }

    nome = tecnicos.get(pk)

    return render(
        request,
        'assistencia/tecnicos/formulario.html',
        {
            'titulo': 'Editar técnico',
            'modo': 'editar',
            'tecnico_id': pk,
            'nome_tecnico': nome,
        }
    )