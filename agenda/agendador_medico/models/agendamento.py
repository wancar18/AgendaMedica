"""
Modelo para gerenciamento de agendamentos no sistema.
Fornece funcionalidades para criar, ler, atualizar e deletar agendamentos no banco de dados.
"""

from models.database import Database

class Agendamento:
    """
    Classe para gerenciar os agendamentos no sistema.
    Implementa operações CRUD (Create, Read, Update, Delete) para agendamentos.
    """
    
    def __init__(self):
        """
        Inicializa a classe Agendamento com uma conexão ao banco de dados.
        """
        self.db = Database()
    
    def agendar_consulta(self, nome_paciente, cpf, especialidade, medico_id, dia, hora):
        """
        Agenda uma nova consulta no sistema.
        
        Args:
            nome_paciente (str): Nome do paciente.
            cpf (str): CPF do paciente.
            especialidade (str): Especialidade médica.
            medico_id (int): ID do médico.
            dia (str): Dia da consulta.
            hora (str): Hora da consulta.
            
        Returns:
            dict: Resultado da operação com status e mensagem.
        """
        # Normaliza o dia e hora para evitar problemas de comparação
        dia_normalizado = dia.strip() if dia else ""
        hora_normalizada = hora.strip() if hora else ""
        
        # Verifica se o horário já está ocupado
        query_verificacao = """
            SELECT COUNT(*) as count FROM agendamentos
            WHERE medico_id = %s AND TRIM(dia) = %s AND TRIM(hora) = %s
        """
        resultado = self.db.execute_single(query_verificacao, (medico_id, dia_normalizado, hora_normalizada))
        
        if resultado and resultado['count'] > 0:
            return {'success': False, 'message': 'Horário já está ocupado.'}
        
        try:
            query_insercao = """
                INSERT INTO agendamentos (nome_paciente, cpf, especialidade, medico_id, dia, hora)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            sucesso = self.db.execute_non_query(query_insercao, (
                nome_paciente, cpf, especialidade, medico_id, dia_normalizado, hora_normalizada
            ))
            
            if sucesso:
                return {'success': True}
            else:
                return {'success': False, 'message': 'Erro ao inserir agendamento no banco de dados.'}
        except Exception as e:
            return {'success': False, 'message': str(e)}
    
    def buscar_por_cpf(self, cpf):
        """
        Busca todos os agendamentos de um paciente pelo CPF.
        
        Args:
            cpf (str): CPF do paciente.
            
        Returns:
            list: Lista de agendamentos do paciente.
        """
        query = """
            SELECT a.id, a.nome_paciente, a.cpf, a.especialidade, a.medico_id, 
                   m.nome as medico_nome, a.dia, a.hora
            FROM agendamentos a
            JOIN medicos m ON a.medico_id = m.id
            WHERE a.cpf = %s
            ORDER BY a.dia, a.hora
        """
        return self.db.execute_query(query, (cpf,))
    
    def buscar_por_medico(self, medico_id):
        """
        Busca todos os agendamentos de um médico pelo ID.
        
        Args:
            medico_id (int): ID do médico.
            
        Returns:
            list: Lista de agendamentos do médico.
        """
        query = """
            SELECT a.id, a.nome_paciente, a.cpf, a.especialidade, a.medico_id, 
                   m.nome as medico_nome, a.dia, a.hora
            FROM agendamentos a
            JOIN medicos m ON a.medico_id = m.id
            WHERE a.medico_id = %s
            ORDER BY a.dia, a.hora
        """
        return self.db.execute_query(query, (medico_id,))
    
    def buscar_horarios_disponiveis(self, medico_id, dia):
        """
        Busca os horários disponíveis para um médico em um determinado dia.
        
        Args:
            medico_id (int): ID do médico.
            dia (str): Dia para verificar disponibilidade.
            
        Returns:
            list: Lista de horários disponíveis.
        """
        # Busca os horários cadastrados para o médico
        query_horarios = "SELECT horarios_atendimento FROM medicos WHERE id = %s"
        medico = self.db.execute_single(query_horarios, (medico_id,))
        
        if not medico or not medico['horarios_atendimento']:
            return []
        
        # Obtém a lista de horários do médico
        horarios = [h.strip() for h in medico['horarios_atendimento'].split(',') if h.strip()]
        
        # Normaliza o dia para comparação
        dia_normalizado = dia.strip() if dia else ""
        
        # Busca os horários já agendados para o médico no dia especificado
        query_agendados = """
            SELECT hora FROM agendamentos
            WHERE medico_id = %s AND TRIM(dia) = %s
        """
        agendados = self.db.execute_query(query_agendados, (medico_id, dia_normalizado))
        
        # Formata os horários agendados para comparação
        horas_agendadas = []
        for a in agendados:
            h = a['hora']
            # Padroniza o formato do horário para HH:MM
            if isinstance(h, str):
                hora_minuto = h.strip()[:5]  # Pega apenas HH:MM e remove espaços
            else:
                # Se for um objeto time ou outro tipo, converte para string no formato HH:MM
                hora_minuto = f"{h.hour:02d}:{h.minute:02d}" if hasattr(h, 'hour') else str(h)[:5]
            horas_agendadas.append(hora_minuto)
        
        # Filtra os horários disponíveis (não agendados)
        disponiveis = [h for h in horarios if h.strip() not in horas_agendadas]
        
        return disponiveis
    
    def alterar_consulta(self, consulta_id, campo, valor, medico_nome=None):
        """
        Altera um campo específico de uma consulta.
        
        Args:
            consulta_id (int): ID da consulta a ser alterada.
            campo (str): Campo a ser alterado ('medico_id', 'dia' ou 'hora').
            valor (str): Novo valor para o campo.
            medico_nome (str, optional): Nome do médico (apenas quando campo='medico_id').
            
        Returns:
            dict: Resultado da operação com status e mensagem.
        """
        try:
            # Verificar se o horário já está ocupado (se estiver alterando hora ou dia)
            if campo in ['hora', 'dia']:
                # Buscar informações da consulta atual
                query_consulta = """
                    SELECT medico_id, dia, hora FROM agendamentos WHERE id = %s
                """
                consulta_atual = self.db.execute_single(query_consulta, (consulta_id,))
                
                if not consulta_atual:
                    return {'success': False, 'message': 'Consulta não encontrada'}
                
                # Preparar os parâmetros para verificação de disponibilidade
                medico_id = consulta_atual['medico_id']
                dia = consulta_atual['dia'] if campo != 'dia' else valor
                hora = consulta_atual['hora'] if campo != 'hora' else valor
                
                # Verificar se o horário já está ocupado
                query_verificacao = """
                    SELECT COUNT(*) as count FROM agendamentos
                    WHERE medico_id = %s AND TRIM(dia) = %s AND TRIM(hora) = %s AND id != %s
                """
                resultado = self.db.execute_single(query_verificacao, (
                    medico_id, dia.strip(), hora.strip(), consulta_id
                ))
                
                if resultado and resultado['count'] > 0:
                    return {'success': False, 'message': 'Horário já está ocupado'}
            
            # Atualizar a consulta
            if campo == 'medico_id' and medico_nome:
                # Se estiver alterando o médico, também atualiza o nome do médico
                query_atualizacao = """
                    UPDATE agendamentos
                    SET medico_id = %s, medico_nome = %s
                    WHERE id = %s
                """
                sucesso = self.db.execute_non_query(query_atualizacao, (valor, medico_nome, consulta_id))
            else:
                # Atualização normal
                query_atualizacao = f"UPDATE agendamentos SET {campo} = %s WHERE id = %s"
                sucesso = self.db.execute_non_query(query_atualizacao, (valor, consulta_id))
            
            if sucesso:
                return {'success': True}
            else:
                return {'success': False, 'message': 'Erro ao atualizar consulta no banco de dados.'}
        except Exception as e:
            return {'success': False, 'message': str(e)}
    
    def cancelar_consulta(self, consulta_id):
        """
        Cancela (remove) uma consulta do sistema.
        
        Args:
            consulta_id (int): ID da consulta a ser cancelada.
            
        Returns:
            dict: Resultado da operação com status e mensagem.
        """
        try:
            query = "DELETE FROM agendamentos WHERE id = %s"
            sucesso = self.db.execute_non_query(query, (consulta_id,))
            
            if sucesso:
                return {'success': True}
            else:
                return {'success': False, 'message': 'Erro ao cancelar consulta.'}
        except Exception as e:
            return {'success': False, 'message': str(e)}
