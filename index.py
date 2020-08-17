from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('Recipe_list.html')


@app.route('/recipes')
def reciped_list():
  return 'Recipes'

@app.route('/recipes/<recipe>')
def selectRecipe(recipe):
  return '{} Recipe'.format(escape(recipe))

@app.route('/<recipe>')
def hello(recipe=None):
  return render_template('single_recipe_page.html', recipe=recipe)