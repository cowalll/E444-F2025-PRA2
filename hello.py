from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime, timezone

app = Flask(__name__)
Bootstrap(app)
Moment(app)

@app.route('/')
def index():
    print(datetime.now(timezone.utc))
    return render_template('index.html', 
                           current_time=datetime.now(timezone.utc))

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500