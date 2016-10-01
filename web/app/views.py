from flask import Blueprint

demo = Blueprint('demo', __name__, url_prefix='/')


@demo.route('/', methods=['GET'])
def index():
    return 'Hello World'
