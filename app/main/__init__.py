#!/usr/bin/env python
# encoding: utf-8
# Author: aju
# Email: prohorse@live.com
# Last_modify: 2015-03-14 21:10:38
# Filename: __init__.py

from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
