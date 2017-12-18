from flask import Blueprint
admin = Blueprint('admin',__name__,template_folder='pages',static_folder='static')

from . import views