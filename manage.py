#!/usr/bin/env python
# encoding: utf-8
# Author: aju
# Email: prohorse@live.com
# Last_modify: 2015-03-14 21:08:30
# Filename: manage.py

from app import create_app, mongo
# from app.models import User, Role
from flask.ext.script import Manager, Shell

app = create_app('development')
manager = Manager(app)

def make_shell_context():
    # return dict(app=app, db=mongo, User=User, Role=Role)
    return dict(app=app, db=mongo)

manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
