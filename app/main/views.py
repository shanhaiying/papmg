#!/usr/bin/env python
# encoding: utf-8
# Author: aju
# Email: prohorse@live.com
# Last_modify: 2015-03-14 21:11:25
# Filename: views.py

from datetime import datetime
from flask import render_template, session, redirect, url_for, flash, request

from . import main
from .. import mongo
from .forms import NameForm, QuestionForm
from ..models import User, Question


@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User(form.name.data)
        had_user = user.get_from_username()
        if not had_user:
            user.save()
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data

        return redirect(url_for('.index'))
    return render_template('index.html',
                           form=form, name=session.get('name'),
                           known=session.get('known', False),
                           current_time=datetime.now())


@main.route('/add_question', methods=['GET', 'POST'])
def add_question():
    form = QuestionForm()
    if form.validate_on_submit():
        question = Question(form.subject.data,
                            form.qtype.data,
                            form.difficulty.data,
                            form.question.data,
                            form.answer.data,
                            'admin')
        question.save()
        flash(u'题目已添加。', 'info')
        return redirect(url_for('.add_question'))
    return render_template('questions.html', form=form)


@main.route('/question_list', methods=['GET', 'POST'])
def all_questions():
    questions = mongo.db.questions.find().sort([('create_time', -1), ])
    return render_template('question_list.html', questions=questions,
                           current_time=datetime.now())
