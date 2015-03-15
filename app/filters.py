#!/usr/bin/env python
# encoding: utf-8
# Author: aju
# Email: prohorse@live.com
# Last_modify: 2015-03-15 17:52:26
# Filename: filters.py

"""
自定义过滤器
"""
from .defines import QUESTION_TYPES, SUBJECTS, DIFFICULTIES

def format_datatime(value, format='%Y-%m-%d %H:%M:%S'):
    return value.strftime(format)

def get_cn_name(value):
    _temp = list()
    _temp.extend(QUESTION_TYPES)
    _temp.extend(SUBJECTS)
    _temp.extend(DIFFICULTIES)
    return dict(_temp).get(value, u"未知名称")
