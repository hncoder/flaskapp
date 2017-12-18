from . import api
from flask import jsonify

@api.route('/a')
def a():
	return jsonify({'data':{},'code':0,'msg':'ok'})