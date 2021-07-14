import csv, os
from os.path import exists
from http import HTTPStatus
from services import CsvServices

# ERRO PARA COLUNAS INVÁLIDAS
class InvalidColumnFilter(ValueError):
    pass

# ERRO PRA QUANDO NENHUM DADO FOR ENCONTRADO
class NotFound(ValueError):
    
    # try:
    #     return CsvServices.top_teen()

    # except:
    #     return {"error": "No results"}, HTTPStatus.BAD_REQUEST
    pass

# ERRO, CASO O USUÁRIO NÃO PASSAR NENHUM, OU 1, ARGS NA ROTA
class MissingArgs(AttributeError):
    pass