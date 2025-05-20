"""
Arquivo principal do sistema de agendamento médico.
Ponto de entrada da aplicação que inicializa o servidor Flask.

Este arquivo é responsável por criar a instância da aplicação Flask
e iniciar o servidor web quando executado diretamente.
"""

from utils.app_factory import create_app

# Cria a aplicação Flask usando a factory
app = create_app()

if __name__ == '__main__':
    """
    Inicia o servidor Flask quando o script é executado diretamente.
    
    O servidor é iniciado em modo de debug para facilitar o desenvolvimento,
    com host definido como 0.0.0.0 para permitir acesso externo.
    """
    app.run(debug=True, host='0.0.0.0')
