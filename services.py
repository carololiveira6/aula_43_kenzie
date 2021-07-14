import csv
from itertools import islice
from json import dump, load
from operator import ne
from custom_errors import InvalidColumnFilter, NotFound, MissingArgs

# Caso queira utilizar Raise com erros customizados
# from custom_errors import InvalidColumnFilter, NotFound, MissingArgs


class CsvServices:
    VALID_FILTERS = ("Name", "Platform",)
    FILEPATH = '/games.csv'

    # CRIE AQUI UM MÉTODO DE INSTANCIA CHAMADO - validate_fields
    # Esse método deve verificar se existe os 2 argumentos na URL
    # Caso exista somente 1 argumente, ou nenhum, retornar um erro dizendo
    # que está faltando argumento(s).

    def validate_fields():


        pass

    # CRIE AQUI UM MÉTODO DE INSTANCIA CHAMADO -validate_column_filter
    # Esse método deve verificar se o argumento column
    # passado atráves da url é um filtro válido.


    # CRIE AQUI UM MÉTODO DE INSTANCIA CHAMADO - found_by_filter
    # Caso haja os 2 argumentos na rota e o filtro por coluna seja válido
    # Esse método deve aplicar os filtros e retornar uma LISTA DE DICIONÁRIOS
    # com os valores filtrado. Caso não encontre nenhum valor após aplicar o filtro
    # deve retornar um erro dizendo que não encontrou nada.


    @staticmethod
    # CRIE AQUI UM MÉTODO ESTÁTICO CHAMADO - top_teen
    # Esse método deve retornar os 10 primeiros games do CSV
    def top_teen():

        with open('/games.csv', newline='') as file:
            reader = csv.DictReader(file)
            for row in islice(reader, 10):
                return row


if __name__ == '__main__':
    filename = '/games.csv'

    top_teen = CsvServices.top_teen(filename)
    print(top_teen)