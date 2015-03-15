#!/usr/bin/env python
# encoding: utf-8
# Author: aju
# Email: prohorse@live.com
# Last_modify: 2015-03-14 21:10:13
# Filename: __init__.py

from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.pymongo import PyMongo
from inspect import getmembers, isfunction
from app import filters

from config import config

bootstrap = Bootstrap()
moment = Moment()
mongo = PyMongo()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    coustom_filters = {name: function
                       for name, function in getmembers(filters)
                       if isfunction(function)}

    bootstrap.init_app(app)
    moment.init_app(app)
    mongo.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    app.jinja_env.filters.update(coustom_filters)

    return app
