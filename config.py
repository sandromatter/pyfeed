#---------------------------------------------------------------------------------------
# 
# config.py
# 
#---------------------------------------------------------------------------------------
# Import packages
#---------------------------------------------------------------------------------------
# Source, working with .env in Flask:
# https://prettyprinted.com/tutorials/automatically_load_environment_variables_in_flask
# https://realpython.com/flask-by-example-part-1-project-setup/

import os


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get("SECRET_KEY")

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True