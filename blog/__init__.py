from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from blog.config import Config


# app.config['SECRET_KEY'] = 'ad635fa5bef52425647233b1ab80d109'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view='users.login' #for making account section to be visible only if the user is logged_in
login_manager.login_message_category = 'info' #displaying the login required message in nice way

#Mailing configuration
# app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = "malviya001raj@gmail.com"
# app.config['MAIL_PASSWORD'] = "yxop mlxr ldxe lzmz"
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