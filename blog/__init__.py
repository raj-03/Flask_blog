from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from blog.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view='users.login' #for making account section to be visible only if the user is logged_in
login_manager.login_message_category = 'info' #displaying the login required message in nice way

mail = Mail() #initializing the instance

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from blog.users.routes import users
    from blog.posts.routes import posts
    from blog.main.routes import main
    from blog.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app