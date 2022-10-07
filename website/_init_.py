from flask import Flask

def create_app():
    app = Flask(__name__) #create flask app
    app.config['SECRET_KEY'] = 'thisisasecretkey' #initialize key

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth/')

    return app