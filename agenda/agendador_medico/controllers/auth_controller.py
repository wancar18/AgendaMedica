"""
Controlador de autenticação para o sistema de agendamento médico.
Gerencia rotas relacionadas a login, logout e verificação de sessão.
"""

from flask import Blueprint, render_template_string, request, redirect, url_for, session
from models.autenticacao import Autenticacao
from views.templates import login_template

# Criação do blueprint para rotas de autenticação
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    """
    Rota principal que exibe a página de login e processa tentativas de autenticação.
    
    Returns:
        str: Página de login renderizada ou redirecionamento para o menu principal.
    """
    erro = None
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        
        # Verifica as credenciais usando o modelo de autenticação
        if Autenticacao.verificar_credenciais(usuario, senha):
            session['logado'] = True
            return redirect(url_for('admin.menu'))
        else:
            erro = 'Usuário ou senha incorretos.'
    
    # Renderiza o template de login
    return render_template_string(login_template, erro=erro)

@auth_bp.route('/logout', methods=['POST'])
def logout():
    """
    Rota para realizar o logout do usuário, limpando a sessão.
    
    Returns:
        redirect: Redirecionamento para a página de login.
    """
    session.clear()
    return redirect(url_for('auth.login'))

def login_required(view_func):
    """
    Decorador para proteger rotas que exigem autenticação.
    
    Args:
        view_func (function): Função de visualização a ser protegida.
        
    Returns:
        function: Função decorada que verifica a autenticação antes de executar a view.
    """
    def wrapped_view(*args, **kwargs):
        if not session.get('logado'):
            return redirect(url_for('auth.login'))
        return view_func(*args, **kwargs)
    
    # Preserva o nome e docstring da função original
    wrapped_view.__name__ = view_func.__name__
    wrapped_view.__doc__ = view_func.__doc__
    
    return wrapped_view
