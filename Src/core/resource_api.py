'''
    MODULO COM CLASSE DE RESOURCE API
'''
from flask_restful import Resource

class ResourceApi(Resource):
    '''CLASSE PARA TRATAMENTO ESPECIFICO DE RESOURCE'''

    def __init__(self):
        super()