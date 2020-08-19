from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('Recipe_list.html')

class Recipe:
  def __init__(self, title, duration, steps):
    self.title = title
    self.duration = duration
    self.steps = steps

recipe_list = [
  Recipe("Egg rice", "45 min", [
    "1 cup rice , uncooked or 3 cups cooked rice",
    "1½ tsp vinegar (adjust to taste)(I use apple cider)",
    "1½ tsp soya sauce (adjust to taste) (use organic)",
    "1 to 2 cloves garlic finely chopped",
    "1/8 tsp crushed pepper or pepper powder",
    "Salt as needed",
    "1 ½ tbsp Olive oil or sesame oil",
    "3 tbsp spring onions chopped, (green and whites separated)",
    "1 medium carrot chopped (optional)",
    "½ cup capsicum small / bell peppers cubed",
    "½ cup cabbage shredded (optional)",
    "3 eggs small or 2 large"
  ]),
  Recipe("Modaka", "1 hour", [
    "2 cups grated coconut (fresh or frozen) (200 grams)",
    "1 cup JAGGERY grated or powdered (125 to 150 grams)",
    "4 green cardamoms powdered (½ teaspoon)",
    "⅛ teaspoon nutmeg powder (optional)",
    "1 teaspoon GHEE",
    "1 cup rice flour (fine flour) (150 grams, Refer notes)",
    "1 cup water (2 to 3 tablespoons more to knead)",
    "1 pinch salt",
    "1 teaspoon GHEE",
    "1 teaspoon GHEE (use as needed)"
  ])
]

@app.route('/<recipe>')
def single_recipe(recipe=None):

  selectedRecipe = False

  for x in recipe_list:
    if x.title == recipe:
      selectedRecipe = x
      return

  return render_template('single_recipe_page.html', recipe=selectedRecipe)