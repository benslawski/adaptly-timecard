## flask modules
from flask import Flask
from flask import request, Response
from flask import render_template
from flask import make_response
from flask import g
from flask import redirect
from flask import session
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import *
from flask.ext.security.datastore.sqlalchemy import SQLAlchemyUserDatastore

## python modules
from werkzeug import secure_filename
import os

## local modules
from DBInterface import *


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'VKqerq3E/adf23d0444'


@app.route('/', methods=['GET'])
def show_card():
    jobs = getJobs()
    return render_template('card.html', jobs=jobs)

@app.route('/punch/', methods=['POST'])
def punch():
    in_time = request.form['in_time'];
    out_time = request.form['out_time'];
    selected_job = request.form['selected_job']
    print 'punch\t', selected_job
    print in_time
    print out_time
    punchCard(selected_job, in_time, out_time) 
    return redirect('/')


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
