"""
Arquivo de inicialização do sistema de agendamento médico.
Configura e inicializa a aplicação Flask.
"""

from flask import Flask
from flask import session

def create_app():
    """
    Cria e configura a aplicação Flask.
    
    Returns:
        Flask: Aplicação Flask configurada.
    """
    app = Flask(__name__)
    
    # Configuração da chave secreta para sessões
    from config.config import SECRET_KEY
    app.secret_key = SECRET_KEY
    
    # Registrar blueprints (rotas)
    from controllers.auth_controller import auth_bp
    from controllers.admin_controller import admin_bp
    from controllers.agendamento_controller import agendamento_bp
    from controllers.api_controller import api_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(agendamento_bp)
    app.register_blueprint(api_bp)
    
    return app
