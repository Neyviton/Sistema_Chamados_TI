
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
    