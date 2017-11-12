# import dependencies
from flask import Flask
from flask_cache import Cache

# create WSGI application object
app = Flask('extranet')

# load configuration
app.config.from_object('extranet.config')

# load database
from extranet.db import db

# load database models
import extranet.models

# load login manager (named as User Session Manager)
from extranet.usm import usm

# load cache
cache = Cache(app)

# load external connections
import extranet.connections

# load modules
from extranet.modules.auth import bp as auth_module
from extranet.modules.oauthprovider import bp as oauthprovider_module
from extranet.modules.api.v0 import bp as api_v0_module

# register modules
app.register_blueprint(auth_module)
app.register_blueprint(oauthprovider_module)
app.register_blueprint(api_v0_module)

# load hooks & cli
import extranet.hooks
import extranet.cli


# simple index page
from flask import render_template
@app.route('/')
def index():
  return render_template('index.html')
from flask_login import login_required
@app.route('/profile/')
@login_required
def profile():
  return render_template('profile.html')