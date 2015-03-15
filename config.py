#!/usr/bin/env python
# encoding: utf-8
# Author: aju
# Email: prohorse@live.com
# Last_modify: 2015-03-14 21:08:09
# Filename: config.py

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'hello_mima'
    FLASK_ADMIN = 'root'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE = ''


class TestingConfig(Config):
    TESTING = True
    DATABASE = ''


class ProductionConfig(Config):
    DATABASE = ''


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
