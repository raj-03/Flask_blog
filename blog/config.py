import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')


    #Mailing configuration
    # app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "malviya001raj@gmail.com"
    MAIL_PASSWORD = "yxop mlxr ldxe lzmz"