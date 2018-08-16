#!/usr/bin/env python3
# (c) 2015 John Strickler
#
import os

class BaseConfig(object):
    SECRET_KEY = 'My hovercraft is full of eels'
    SPAMHAMMER_MAIL_PREFIX = '[SpamHammer]'
    SPAMHAMMER_MAIL_SENDER = 'SpamHammer Admin <admin@spamhammer.com>'

    @staticmethod
    def init_app(app):
        pass

class DevConfig(BaseConfig):
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    DB_URI = os.environ.get('DEV_DATABASE_URL')

class ProdConfig(BaseConfig):
    DB_URI = os.environ.get('DATABASE_URL')

# not really needed...
config = {
    'development': DevConfig,
    'production': ProdConfig,
    'default': DevConfig
}
