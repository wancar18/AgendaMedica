"""
Controlador para agendamentos no sistema de agendamento médico.
Gerencia rotas relacionadas ao agendamento de consultas.
"""

from flask import Blueprint, render_template_string
from controllers.auth_controller import login_required
from views.templates import agendamentos_template

# Criação do blueprint para rotas de agendamento
agendamento_bp = Blueprint('agendamento', __name__)

@agendamento_bp.route('/agendamentos')
@login_required
def agendamentos():
    """
    Rota para exibir a página de agendamentos.
    Mostra a interface de chat para agendamento, alteração e cancelamento de consultas.
    
    Returns:
        str: Página de agendamentos renderizada.
    """
    return render_template_string(agendamentos_template)
