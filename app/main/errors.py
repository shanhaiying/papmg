#!/usr/bin/env python
# encoding: utf-8
# Author: aju
# Email: prohorse@live.com
# Last_modify: 2015-03-14 21:11:46
# Filename: errors.py

from flask import render_template
from . import main

@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
