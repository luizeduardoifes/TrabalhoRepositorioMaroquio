import sqlite3

def obter_conexao():
    """Estabelece uma conexão com o banco de dados SQLite."""
    conexao = sqlite3.connect('dados.db')
    return conexao