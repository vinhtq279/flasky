from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Hello World!</h1>'

@app.route('/user/<int:id>')
def user(id):
	return '<h1>Hello {}</h1>'.format(id)
