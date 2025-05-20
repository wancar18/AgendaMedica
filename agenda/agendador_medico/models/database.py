"""
Modelo para gerenciamento de conexão com o banco de dados.
Fornece funcionalidades para conectar e interagir com o banco de dados MySQL.
"""

import mysql.connector
from config.config import DB_CONFIG

class Database:
    """
    Classe para gerenciar a conexão com o banco de dados MySQL.
    Implementa o padrão Singleton para garantir uma única instância de conexão.
    """
    
    _instance = None
    
    def __new__(cls):
        """
        Implementação do padrão Singleton para garantir uma única instância da conexão.
        
        Returns:
            Database: Instância única da classe Database.
        """
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._connect()
        return cls._instance
    
    def _connect(self):
        """
        Estabelece a conexão com o banco de dados MySQL usando as configurações definidas.
        """
        self.connection = mysql.connector.connect(**DB_CONFIG)
        self.cursor = self.connection.cursor(dictionary=True)
    
    def execute_query(self, query, params=None):
        """
        Executa uma consulta SQL no banco de dados.
        
        Args:
            query (str): Consulta SQL a ser executada.
            params (tuple, optional): Parâmetros para a consulta SQL. Defaults to None.
            
        Returns:
            list: Resultado da consulta em formato de dicionário.
        """
        try:
            self.cursor.execute(query, params or ())
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Erro ao executar consulta: {e}")
            return []
    
    def execute_single(self, query, params=None):
        """
        Executa uma consulta SQL e retorna apenas o primeiro resultado.
        
        Args:
            query (str): Consulta SQL a ser executada.
            params (tuple, optional): Parâmetros para a consulta SQL. Defaults to None.
            
        Returns:
            dict: Primeiro resultado da consulta em formato de dicionário.
        """
        try:
            self.cursor.execute(query, params or ())
            return self.cursor.fetchone()
        except Exception as e:
            print(f"Erro ao executar consulta: {e}")
            return None
    
    def execute_non_query(self, query, params=None):
        """
        Executa uma consulta SQL que não retorna resultados (INSERT, UPDATE, DELETE).
        
        Args:
            query (str): Consulta SQL a ser executada.
            params (tuple, optional): Parâmetros para a consulta SQL. Defaults to None.
            
        Returns:
            bool: True se a operação foi bem-sucedida, False caso contrário.
        """
        try:
            self.cursor.execute(query, params or ())
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Erro ao executar consulta: {e}")
            return False
    
    def get_last_id(self):
        """
        Obtém o ID da última linha inserida.
        
        Returns:
            int: ID da última linha inserida.
        """
        return self.cursor.lastrowid
    
    def close(self):
        """
        Fecha a conexão com o banco de dados.
        """
        if hasattr(self, 'connection') and self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
