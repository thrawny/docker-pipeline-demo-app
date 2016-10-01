from flask import Flask

from config import config


def create_app(environment):
    app = Flask(__name__)
    app.config.from_object(config[environment])

    from .views import demo
    app.register_blueprint(demo)

    return app
