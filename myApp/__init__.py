# python package
from flask import Flask
from config import DevConfig
from flask_migrate import Migrate

def create_app(config_class=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)


    # Initialize Flask extensions
    from myApp.db import db # Import the db object and various models that have inherited the db object
    db.init_app(app)
    migrate = Migrate(app, db)


    # Register blueprints here
    from myApp.views.users.bp import bp as admin_bp
    app.register_blueprint(admin_bp,url_prefix='/admin')



    @app.route('/health/')
    def test_page():
        return 'PONG'


    return app

