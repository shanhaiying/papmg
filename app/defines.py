#!/usr/bin/env python
# encoding: utf-8
# Author: aju
# Email: prohorse@live.com
# Last_modify: 2015-03-15 16:08:48
# Filename: defines.py

"""
通用常量定义模块
"""

# 题目类型
QUESTION_TYPES = [
    ('single', u'单选题'),
    ('multiple', u'多选题'),
    ('judge', u'判断题'),
    ('fill', u'填空题'),
    ('qa', u'问答题'),
]

# 所属学科
SUBJECTS = [
    ('program', u'程序设计'),
    ('datastruct', u'数据结构'),
    ('algorithm', u'算法分析'),
    ('advmath', u'高等数学'),
]


# 难度系数
DIFFICULTIES = [
    ('1', u'普通难度'),
    ('2', u'噩梦难度'),
    ('4', u'地狱难度'),
    ('8', u'炼狱难度'),
]
