from flask import Flask
from typing import Tuple
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from db.connection import conn_string
from flask_cors import CORS
from flask import url_for



def create_app() -> Tuple[Flask, SQLAlchemy]:
    """Create and configure the app.

    Args:
        config: configuration parameter

    Returns:
        the application instance

    """

    # Flask Application Configuration
    app = Flask(__name__)

    # SQL Alchemy Config
    app.config["SQLALCHEMY_DATABASE_URI"] = conn_string
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    sql_app = SQLAlchemy(app)
    CORS(app)


    return app, sql_app


# initialize and set configuration
app, sql = create_app()


# Flask Restx
class HttpsTerminatedApi(Api):
    """Override API class with _scheme = 'https' option in spec property."""

    @property
    def specs_url(self):
        """Monkey patch for HTTPS"""
        scheme = "http" if "5000" in self.base_url else "https"
        return url_for(self.endpoint("specs"), _external=True, _scheme=scheme)


api = HttpsTerminatedApi(
    version="1.0",
    title="Feature Toggle API",
    description="API for managing feature toggles",
)
