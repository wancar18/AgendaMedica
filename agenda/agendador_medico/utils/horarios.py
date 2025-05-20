"""
Utilitários para o sistema de agendamento médico.
Contém funções auxiliares utilizadas em diversas partes do sistema.
"""

def gerar_horarios():
    """
    Gera uma lista de horários disponíveis para agendamento no formato HH:MM.
    
    Returns:
        list: Lista de strings representando horários no formato HH:MM, de 30 em 30 minutos.
    """
    horarios = []
    for hora in range(24):
        for minuto in (0, 30):
            horarios.append(f"{hora:02d}:{minuto:02d}")
    return horarios

# Lista de horários disponíveis para agendamento
HORARIOS = gerar_horarios()
