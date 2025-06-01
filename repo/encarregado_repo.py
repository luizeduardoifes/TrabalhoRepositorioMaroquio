from models.encarregado import Ecarregado
from sql.encarregado_sql import CRIAR_TABELA_ENCARREGADO
from data.database import obter_conexao

def criar_tabela_encarregado():
    """Cria a tabela 'encarregado' no banco de dados."""
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(CRIAR_TABELA_ENCARREGADO)
    conexao.commit()
    conexao.close()

    