# application.py


from flask import Blueprint
from rest_wrapper import api
from endpoints.toggle_features import ns as toggle_ns
from rest_wrapper import app

#Flask Restx 

blueprint = Blueprint("api", __name__)
api.init_app(blueprint)
api.add_namespace(toggle_ns)
app.register_blueprint(blueprint)


if __name__ == '__main__':
    app.run()
