#!/usr/bin/env python
# -*- coding:utf-8 -*-

from app import app
from app.extensions import mongo
from app.models import Item, User
from flask.ext.script import Manager, Shell
import sys

# 设置系统编码
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=mongo.db, Item=Item, User=User)


manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
