from flask import Flask, request, jsonify, Blueprint
import json
from flask_sqlalchemy import SQLAlchemy
from application.Config import Config



# creates the app and sets configurations 
def create_app(config_class={}):
    '''creates the app and sets configurations. Depending on the the config '''
    app =  Flask (__name__)
 
    config_class = config_class or Config
    app.config.from_object(config_class)

    return app




class ReverseProxied(object):
    ''' This method is used to Force HTTP/HTTPS redirects'''
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        scheme = environ.get('HTTP_X_FORWARDED_PROTO')
        if scheme:
            environ['wsgi.url_scheme'] = scheme
        return self.app(environ, start_response)


application = app = create_app()
app.wsgi_app = ReverseProxied(app.wsgi_app)
app.config['SQLALCHEMY_DATABASE_URI'] =  "mysql+pymysql://peter:foxfordccl9379@budgetdb.cozn4jwwelqb.eu-west-1.rds.amazonaws.com:3306/budgetSchema"

db = SQLAlchemy(app)



from application.main.routes import main
app.register_blueprint(main)

  