#!/usr/bin/env python
# encoding: utf-8
# Author: aju
# Email: prohorse@live.com
# Last_modify: 2015-03-14 21:13:58
# Filename: models.py

"""
数据模型
"""

from datetime import datetime
from bson import ObjectId
from . import mongo

class User:
    def __init__(self, username, role_id=None):
        self.username = username
        self.role_id = role_id

    def get_from_username(self):
        user = mongo.db.users.find_one({'username': self.username})
        return user

    def save(self):
        mongo.db.users.save(self.__dict__)


class Role:
    def __init__(self, rolename):
        self.rolename = rolename

    def get_from_rolename(self):
        role = mongo.db.roles.find_one({'rolename': self.rolename})
        return role


class Question:
    """
    试题模型
    """
    def __init__(self, subject, qtype, difficulty, question, answer, creator):
        self.subject = subject              # 科目
        self.qtype = qtype                  # 题型（单选、多选、填空、判断、问答）
        self.difficulty = difficulty        # 难度系数（1~10）
        self.question = question            # 问题
        self.answer = answer                # 答案
        self.creator = creator              # 创建人
        self.create_time = datetime.now()   # 添加时间

    @staticmethod
    def get_from_id(_id):
        """
        通过_id获取题目数据的静态方法
        """
        question = mongo.db.questions.find_one({'_id': ObjectId(str(_id))})
        return question

    def save(self):
        mongo.db.questions.save(self.__dict__)

    def update(self, _id, data):
        """
        通过_id更新题目数据
        """
        try:
            mongo.db.questions.update({'_id': ObjectId(str(_id))}, {'$set': dict(data)})
        except:
            raise "_id doesn't exists or data type error"
        return 'OK'

    def remove(self, _id):
        mongo.db.questions.remove({'_id': ObjectId(str(_id))})

