'''
Include all imports in this file; it will be called at the beginning of all files.
'''

from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import g
from flask import url_for
from flask import flash
from flask import abort
from flask_admin import Admin
from app.config import *
from app.models import *
import pprint
import sys
import datetime
cfg = get_cfg()

app = Flask(__name__)
app.secret_key = 'QWEasdzxc!'

# Builds all the database connections on app run

# @app.before_request
# def before_request():
#     g.dbMain =  mainDB.get_conn()

# @app.teardown_request
# def teardown_request(exception):
#     dbM = getattr(g, 'db', None)
#     if (dbM is not None) and (not dbM.is_closed()):
#       dbM.close()
      
# @app.errorhandler(403)
# def access_denied(e):
#     return render_template('views/403.html', cfg=cfg), 403
    
# @app.errorhandler(404)
# def pageNotFound(e):
    # return render_template('views/404.html', cfg=cfg), 404
