from flask_sqlalchemy import SQLAlchemy

# Create db object. This db object will be imported in various model definitions
db = SQLAlchemy()



# Import various models that have inherited the db object and have defined the tables, fiedl, relationships etc
from myApp.models.admin_model import * 


