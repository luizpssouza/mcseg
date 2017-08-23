'''
    MODULO PARA REGISTRO DE BLUEPRINTS
'''
#ALL BLUEPRINTS
from ..blueprints.sample.sample_controller import Sample

def load_routes(__api__):
    '''LOAD ROUTES'''
    __api__.add_resource(Sample, '/sample')
