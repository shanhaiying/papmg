#!/usr/bin/env python
# encoding: utf-8
# Author: aju
# Email: prohorse@live.com
# Last_modify: 2015-03-14 21:11:35
# Filename: forms.py

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms import TextAreaField, HiddenField
from wtforms import RadioField, SelectField
from wtforms.validators import Required

from ..defines import QUESTION_TYPES, SUBJECTS, DIFFICULTIES


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField(u'提交')

class QuestionForm(Form):
    subject = SelectField(u"所属学科", choices=SUBJECTS, validators=[Required()])
    qtype = SelectField(u"题目类型", choices=QUESTION_TYPES, validators=[Required()])
    difficulty = SelectField(u"难度系数", choices=DIFFICULTIES, validators=[Required()])
    question = TextAreaField(u"题目描述", validators=[Required()])
    answer = TextAreaField(u"参考答案", validators=[Required()])
    submit = SubmitField(u'提交')
