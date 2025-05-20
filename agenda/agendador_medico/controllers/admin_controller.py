"""
Controlador para área administrativa do sistema de agendamento médico.
Gerencia rotas relacionadas ao menu principal e parâmetros do sistema.
"""

from flask import Blueprint, render_template_string, request, redirect, url_for
from controllers.auth_controller import login_required
from models.medico import Medico
from views.templates import menu_template, parametros_template, editar_medico_template
from utils.horarios import HORARIOS
from config.config import DIAS_DA_SEMANA

# Criação do blueprint para rotas administrativas
admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/menu')
@login_required
def menu():
    """
    Rota para exibir o menu principal do sistema administrativo.
    
    Returns:
        str: Página de menu renderizada.
    """
    return render_template_string(menu_template)

@admin_bp.route('/parametros')
@login_required
def parametros():
    """
    Rota para exibir a página de parâmetros do sistema.
    Mostra a lista de médicos cadastrados e formulário para cadastro de novos médicos.
    
    Returns:
        str: Página de parâmetros renderizada.
    """
    # Busca todos os médicos cadastrados
    medico_model = Medico()
    medicos = medico_model.listar_todos()
    
    return render_template_string(
        parametros_template, 
        dias_da_semana=DIAS_DA_SEMANA, 
        horarios=HORARIOS, 
        medicos=medicos
    )

@admin_bp.route('/parametros/cadastrar', methods=['POST'])
@login_required
def cadastrar_medico():
    """
    Rota para processar o cadastro de um novo médico.
    
    Returns:
        redirect: Redirecionamento para a página de parâmetros.
    """
    nome_medico = request.form.get('nome_medico')
    crm = request.form.get('CRM')
    especialidade = request.form.get('especialidade')
    dias = request.form.getlist('dias')
    horarios = request.form.getlist('horarios')
    
    # Cadastra o médico usando o modelo
    medico_model = Medico()
    medico_model.cadastrar(nome_medico, crm, especialidade, dias, horarios)
    
    return redirect(url_for('admin.parametros'))

@admin_bp.route('/parametros/editar/<int:medico_id>', methods=['GET', 'POST'])
@login_required
def editar_medico(medico_id):
    """
    Rota para exibir e processar a edição de um médico.
    
    Args:
        medico_id (int): ID do médico a ser editado.
        
    Returns:
        str/redirect: Página de edição renderizada ou redirecionamento para parâmetros.
    """
    medico_model = Medico()
    medico = medico_model.buscar_por_id(medico_id)
    
    if not medico:
        return redirect(url_for('admin.parametros'))

    if request.method == 'POST':
        dias = request.form.getlist('dias')
        horarios = request.form.getlist('horarios')
        
        # Atualiza o médico usando o modelo
        medico_model.atualizar(medico_id, dias, horarios)
        return redirect(url_for('admin.parametros'))

    # Prepara os dados para o template
    dias_selecionados = medico['dias_atendimento'].split(',') if medico['dias_atendimento'] else []
    horarios_selecionados = medico['horarios_atendimento'].split(',') if medico['horarios_atendimento'] else []

    return render_template_string(
        editar_medico_template,
        medico=medico,
        dias_da_semana=DIAS_DA_SEMANA,
        horarios=HORARIOS,
        dias_selecionados=dias_selecionados,
        horarios_selecionados=horarios_selecionados
    )

@admin_bp.route('/parametros/deletar/<int:medico_id>', methods=['POST'])
@login_required
def deletar_medico(medico_id):
    """
    Rota para deletar um médico do sistema.
    
    Args:
        medico_id (int): ID do médico a ser deletado.
        
    Returns:
        redirect: Redirecionamento para a página de parâmetros.
    """
    medico_model = Medico()
    medico_model.deletar(medico_id)
    
    return redirect(url_for('admin.parametros'))
