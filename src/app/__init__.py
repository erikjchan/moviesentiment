import os
from flask import Flask, render_template, jsonify, make_response
import config

# Configure Flask app
app = Flask(__name__, static_url_path='/static')
app.config.from_object(os.environ['APP_SETTINGS'])

# Import + Register Blueprints
from app.irsystem import irsystem as irsystem
app.register_blueprint(irsystem)

# React Catch All Paths
@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')

@app.route('/statistics', methods=['GET'])
def statistics_path():
  return render_template('statistics.html')

@app.route('/now_playing/<path:path>', methods=['GET'])
def now_playing_path(path):
  	return render_template('now_playing.html')

@app.route('/upcoming/<path:path>', methods=['GET'])
def upcoming_path(path):
  	return render_template('upcoming.html')

@app.route('/<path:path>', methods=['GET'])
def any_root_path(path):
  return render_template('index.html')

# HTTP error handling
@app.errorhandler(404)
def not_found(error):
  return render_template('404.html'), 404
