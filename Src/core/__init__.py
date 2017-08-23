''' IMPORT FLASK MODULES '''
from flask import Flask, Blueprint, Request
from flask_restful import Api, url_for
from .routes import load_routes

__app__ = Flask(__name__)
__apiblueprint__ = Blueprint('api', __name__)
__api__ = Api(__apiblueprint__)
__urlfor__ = url_for
__request__ = Request

#CARREGA ROTAS BLUEPRINTS
load_routes(__api__)

#REGISTRANDO BLUEPRINT
__app__.register_blueprint(__apiblueprint__)