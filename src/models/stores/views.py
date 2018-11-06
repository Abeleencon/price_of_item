from flask import Blueprint


__author__ = 'Abiodun'


store_blueprint = Blueprint('stored', __name__)


@store_blueprint.route('/store/<string:name>')
def store_page():
    pass
