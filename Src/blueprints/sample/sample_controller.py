'''
    DOCSTRING DO MODULO
'''
from ...core.resource_api import ResourceApi
from flask import request

class Sample(ResourceApi):
    '''CLASSE DE EXEMPLO'''
    def get(self):
        '''METODO GET'''
        return {'hello': 'world'}

    def post(self):
        '''METODO POST'''
        return {'post': request.form}