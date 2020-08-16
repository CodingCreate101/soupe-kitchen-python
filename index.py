from flask import Flask
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def index():
  return 'Welcome to soup kitchen'

@app.route('/recipes')
def reciped_list():
  return 'Recipes'

@app.route('/recipes/<recipe>')
def selectRecipe(recipe):
  return '{} Recipe'.format(escape(recipe))