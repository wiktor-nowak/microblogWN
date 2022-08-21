import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-hard-to-break=haslo'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db') #sqlite:///microblog/app.db ???
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # TODO 1: Dopytać Kubę o szczegóły >os.environ.get...<
