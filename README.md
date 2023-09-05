# ARCHITECTURING THE FLASK APP
 - CONFIGS: https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy
 - TEMPLATES: https://realpython.com/flask-blueprint/#including-templates
 - FLASK MIGRATE- https://rest-apis-flask.teclado.com/docs/flask_migrate/add_flask_migrate_to_app/
 - https://levelup.gitconnected.com/remove-pycache-vscode-6c9204399913


## MAIN STEPS

### CONFIGURATIONS
- `config.py`: various configuration sets that can be called when initantiating the Flask app
    - Each configuration set includes parameters. Non-secret configurations can be declared. Secret configs can be loaded from .env
- `.env, .env.production`: various secrets that can be injected in each configuration inside config.py


## ORGANZIATION
1. The app directory containes all application logic
2. myApp/__init__.py includes the factory pattern for creation of Flask app
  - `config_class=DevConfig` means it will load the `DevConfig` configuration from `config.py` which loads secrets from `.env`


## Models inheritance / tree
1. Initialize the SQLAlchemy db object in `myApp/db.py` : `db = SQLAlchemy()`
2. Import and inject db object into the app in `myApp/__init__.py` inside the `create_app` factory :  `from myApp.db import db , db.init_app(app)`
3. Creating Models:
    - Create model in `myApp/models/blueprint_model.py`. 
        - First import the `db` object from `myApp/db.py`
        - Create the Model classes 
    - Import the declared model classes in `myApp/db.py` at the bottom (to avoid circular imports): `from myApp.models import admin_models`


## Migrations
1. Import Flask Migrate in `myApp/__init__.py` inside the `create_app` factory
2. Inject the created db and app objects in Migrate db object  `migrate = Migrate(app, db)` 



### Blueprints
1. Create individual Blueprint specific folders inside views oor apis directory. eg admin
2. Create __init__.py inside the blueprint specific folder
3. Create a Blueprint_bp.py file inside the blueprint specific folder
4. Instantiate a blueprint object
5. Add Blueprint Views
6. Register the blueprint with its URL prefix in myApp/__init__.py



## Templates:
- https://realpython.com/flask-blueprint/#including-templates


