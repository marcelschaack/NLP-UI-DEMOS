from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.db import get_db

bp = Blueprint('note', __name__)

@bp.route('/')
def index():
    sentence = ['Tommy came to the hospital on July 21st 2019, \
    diagnosed as', 'common cold', 'no ', 'mononucleosis']
    return render_template('note/index.html', sentence=sentence)


@bp.route('/concept1', methods=('GET', 'POST'))
def concept1():
    if request.method == 'POST':
        error = None
        correct = request.form['correct']
        correct = correct.lower()
        if correct != 'yes' and correct != 'no':
            error = 'Please insert yes or no.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO feedback (correct)'
                ' VALUES (?)',
                ([correct])
            )
            db.commit()
            return redirect(url_for('note.index'))

    return render_template('note/concept1.html')

@bp.route('/concept2', methods=('GET', 'POST'))
def concept2():
    if request.method == 'POST':
        error = None
        correct = request.form['correct']
        correct = correct.lower()
        if correct != 'yes' and correct != 'no':
            error = 'Please insert yes or no.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO feedback (correct)'
                ' VALUES (?)',
                ([correct])
            )
            db.commit()
            return redirect(url_for('note.index'))

    return render_template('note/concept2.html')