import os
from flask import Flask

def create_app(test_config=None):
    #create and config app
    app = Flask(__name__,instance_relative_config=True)
    from . import db
    db.init_app(app)
    from . import auth
    app.register_blueprint(auth.bp)
    app.config.from_mapping(
        SECRET_KEY = 'minh',
        DATABASE=os.path.join(app.instance_path,'flaskr.sqlite'),
    )
    if test_config is None:
        #load instance config
        app.config.from_pyfile('config.py',silent=True)
    else:
        app.config.from_mapping(test_config)
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
