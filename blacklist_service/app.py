from flask import Flask
from flask_restful import Api
from config import Config
from extensions import db, ma, jwt
from routes import AddToBlacklist, Login


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)

    api = Api(app)

    # Definir rutas
    api.add_resource(AddToBlacklist, '/blacklists')
    api.add_resource(Login, '/login')

    # Crear tablas si no existen
    with app.app_context():
        db.create_all()

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
