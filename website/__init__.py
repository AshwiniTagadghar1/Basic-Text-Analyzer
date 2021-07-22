from flask import Flask
import os

def create_app():
    my_path = os.getcwd()
    UPLOAD_FOLDER = my_path+'/website/temp'
    
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['SECRET_KEY'] = 'hiash'
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/') 
    app.register_blueprint(auth,url_prefix='/')
    
    return app