"""
Controlador de API para o sistema de agendamento médico.
Gerencia endpoints da API para comunicação com o frontend.
"""

from flask import Blueprint, request, jsonify
from models.medico import Medico
from models.agendamento import Agendamento

# Criação do blueprint para rotas de API
api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/especialidades')
def api_especialidades():
    """
    Endpoint para listar todas as especialidades médicas disponíveis.
    
    Returns:
        json: Lista de especialidades em formato JSON.
    """
    medico_model = Medico()
    resultados = medico_model.listar_especialidades()
    return jsonify(resultados)

@api_bp.route('/medicos')
def api_medicos():
    """
    Endpoint para listar médicos por especialidade.
    
    Returns:
        json: Lista de médicos da especialidade especificada em formato JSON.
    """
    especialidade = request.args.get('especialidade')
    medico_model = Medico()
    resultados = medico_model.buscar_por_especialidade(especialidade)
    return jsonify(resultados)

@api_bp.route('/dias')
def api_dias():
    """
    Endpoint para listar dias de atendimento de um médico.
    
    Returns:
        json: Lista de dias de atendimento em formato JSON.
    """
    medico_id = request.args.get('medico_id')
    medico_model = Medico()
    dias = medico_model.obter_dias_atendimento(medico_id)
    return jsonify(dias)

@api_bp.route('/horarios')
def api_horarios():
    """
    Endpoint para listar horários de atendimento de um médico.
    
    Returns:
        json: Lista de horários de atendimento em formato JSON.
    """
    medico_id = request.args.get('medico_id')
    medico_model = Medico()
    horarios = medico_model.obter_horarios_atendimento(medico_id)
    return jsonify(horarios)

@api_bp.route('/horarios_disponiveis')
def api_horarios_disponiveis():
    """
    Endpoint para listar horários disponíveis para agendamento com um médico em um dia específico.
    
    Returns:
        json: Lista de horários disponíveis em formato JSON.
    """
    medico_id = request.args.get('medico_id')
    dia = request.args.get('dia')
    
    # Log para debug
    print(f"Buscando horários para médico ID: {medico_id}, Dia: '{dia}'")
    
    agendamento_model = Agendamento()
    disponiveis = agendamento_model.buscar_horarios_disponiveis(medico_id, dia)
    
    print(f"Horários disponíveis: {disponiveis}")
    return jsonify(disponiveis)

@api_bp.route('/consultas')
def api_consultas():
    """
    Endpoint para listar consultas agendadas para um paciente por CPF.
    
    Returns:
        json: Lista de consultas do paciente em formato JSON.
    """
    cpf = request.args.get('cpf')
    if not cpf:
        return jsonify({'error': 'CPF não fornecido'}), 400
    
    agendamento_model = Agendamento()
    consultas = agendamento_model.buscar_por_cpf(cpf)
    return jsonify(consultas)

@api_bp.route('/consultas_por_medico')
def api_consultas_por_medico():
    """
    Endpoint para listar consultas agendadas para um médico específico.
    
    Returns:
        json: Lista de consultas do médico em formato JSON.
    """
    medico_id = request.args.get('medico_id')
    if not medico_id:
        return jsonify({'error': 'ID do médico não fornecido'}), 400
    
    agendamento_model = Agendamento()
    consultas = agendamento_model.buscar_por_medico(medico_id)
    return jsonify(consultas)

@api_bp.route('/alterar_consulta', methods=['POST'])
def api_alterar_consulta():
    """
    Endpoint para alterar uma consulta existente.
    
    Returns:
        json: Resultado da operação em formato JSON.
    """
    data = request.json
    consulta_id = data.get('consulta_id')
    campo = data.get('campo')
    valor = data.get('valor')
    medico_nome = data.get('medico_nome')
    
    if not consulta_id or not campo or valor is None:
        return jsonify({'success': False, 'message': 'Dados incompletos'}), 400
    
    agendamento_model = Agendamento()
    resultado = agendamento_model.alterar_consulta(consulta_id, campo, valor, medico_nome)
    
    if resultado['success']:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'message': resultado['message']}), 500

@api_bp.route('/cancelar_consulta', methods=['POST'])
def api_cancelar_consulta():
    """
    Endpoint para cancelar (remover) uma consulta.
    
    Returns:
        json: Resultado da operação em formato JSON.
    """
    data = request.json
    consulta_id = data.get('consulta_id')
    
    if not consulta_id:
        return jsonify({'success': False, 'message': 'ID da consulta não fornecido'}), 400
    
    agendamento_model = Agendamento()
    resultado = agendamento_model.cancelar_consulta(consulta_id)
    
    if resultado['success']:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'message': resultado['message']}), 500

@api_bp.route('/agendar', methods=['POST'])
def api_agendar():
    """
    Endpoint para agendar uma nova consulta.
    
    Returns:
        json: Resultado da operação em formato JSON.
    """
    data = request.json
    
    agendamento_model = Agendamento()
    resultado = agendamento_model.agendar_consulta(
        data['nome_paciente'],
        data['cpf'],
        data['especialidade'],
        data['medico_id'],
        data['dia'],
        data['hora']
    )
    
    return jsonify(resultado)
