from flask_bootstrap import Bootstrap
from flask import Flask, render_template
app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/user/<name>')
def user(name):
	return render_template('user.html', name=name)

@app.route('/base1/')
def base1():
	return render_template('base1.html')
