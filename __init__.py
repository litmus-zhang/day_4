# Extend your application to more than just one file, and create a scalable project structure, containing a run.py module to run your application, a “main” python package,  that contains a flask application factory. A single flask blueprint called user that will hold all user logic. Also, add a models.py module on the same level as the run.py module. For more information read this:

from flask import Flask
from .user.run  import user


def create_app():
    app = Flask(__name__)

    app.register_blueprint(user)
   

    return app