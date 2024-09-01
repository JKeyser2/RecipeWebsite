import os

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

from flask_sqlalchemy import SQLAlchemy

############################################################################################################

project_dir = os.path.dirname(os.path.abspath(__file__))

database_file = "sqlite:///{}".format(os.path.join(project_dir, "recipe.db"))
recipeApp = Flask(__name__)
recipeApp.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(recipeApp)

class recipeClass(db.Model):
    __tablename__ = 'recipe_view'
    index = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    recipe_name = db.Column(db.String(20), unique=False, nullable=False, primary_key=False)
    rating = db.Column(db.String(20), unique=False, nullable=False, primary_key=False)
    ingredients = db.Column(db.String(20), unique=False, nullable=False, primary_key=False)
    servings = db.Column(db.String(20), unique=False, nullable=False, primary_key=False)
    nutrition = db.Column(db.String(20), unique=False, nullable=False, primary_key=False)
    timing = db.Column(db.String(20), unique=False, nullable=False, primary_key=False)
    directions = db.Column(db.String(20), unique=False, nullable=False, primary_key=False)    

    def __repr__(self):
        return "<Index: {}\tRecipe Name: {}\tImage: {}\tRating: {}\tIngridients: {}\tServings: {}\tNutrition: {}\tTiming: {}\tDirections: {}> ".format(
            self.index, self.recipe_name, self.rating, self.ingredients, self.servings, self.nutrition, self.timing, self.directions)


############################################################################################################

@recipeApp.route('/')
def index():
    return render_template('index.html')

@recipeApp.route('/recipeG', methods=["GET","POST"])
def recipeG():
    guests = recipeClass.query.all()
    return render_template('guestRecipe.html', guests=guests)

############################################################################################################

@recipeApp.route("/recipeA", methods=["GET","POST"])
def addRecipeA():
    if request.form:
        last_idxA = recipeClass.query.order_by(recipeClass.index.desc()).first() 
        idxAddA = last_idxA.index + 1
        
        admin = recipeClass(index=idxAddA,
                    recipe_name=request.form.get("respNameA"),
                    rating=request.form.get("ratingA"),
                    ingredients=request.form.get("ingredientsA"),
                    servings=request.form.get("servingsA"),
                    nutrition=request.form.get("nutritionA"),
                    timing=request.form.get("timingA"),
                    directions=request.form.get("directionsA"))
        
        db.session.add(admin)
        db.session.commit()
    admins = recipeClass.query.all()
    return render_template("adminRecipe.html", admins=admins)

@recipeApp.route("/recipeU", methods=["GET","POST"])
def addRecipeU():
    if request.form:
        last_idxU = recipeClass.query.order_by(recipeClass.index.desc()).first() 
        idxAddU = last_idxU.index + 1
        
        userR = recipeClass(index=idxAddU,
                    recipe_name=request.form.get("respNameU"),
                    rating=request.form.get("ratingU"),
                    ingredients=request.form.get("ingredientsU"),
                    servings=request.form.get("servingsU"),
                    nutrition=request.form.get("nutritionU"),
                    timing=request.form.get("timingU"),
                    directions=request.form.get("directionsU"))
        
        db.session.add(userR)
        db.session.commit()
    userRs = recipeClass.query.all()
    return render_template("userRecipe.html", userRs=userRs)

############################################################################################################

@recipeApp.route("/recipeA/update", methods=["POST"])
def updateRecipeA():
    FindIdxA = request.form.get("FindIdxA")
    newRespNameA = request.form.get("newRespNameA")
    newRatingA = request.form.get("newRatingA")
    newIngredientsA = request.form.get("newIngredientsA")
    newServingsA = request.form.get("newServingsA")
    newNutritionA = request.form.get("newNutritionA")
    newTimingA = request.form.get("newTimingA")
    newDirectionsA = request.form.get("newDirectionsA")

    admin = recipeClass.query.filter_by(index=FindIdxA).first()
    admin.index = FindIdxA
    admin.recipe_name = newRespNameA
    admin.rating = newRatingA
    admin.ingredients = newIngredientsA
    admin.servings = newServingsA
    admin.nutrition = newNutritionA
    admin.timing = newTimingA
    admin.directions = newDirectionsA

    db.session.commit()
    return redirect("/recipeA")

@recipeApp.route("/recipeU/update", methods=["POST"])
def updateRecipeU():
    FindIdxU = request.form.get("FindIdxU")
    newRespNameU = request.form.get("newRespNameU")
    newRatingU = request.form.get("newRatingU")
    newIngredientsU = request.form.get("newIngredientsU")
    newServingsU = request.form.get("newServingsU")
    newNutritionU = request.form.get("newNutritionU")
    newTimingU = request.form.get("newTimingU")
    newDirectionsU = request.form.get("newDirectionsU")

    userR = recipeClass.query.filter_by(index=FindIdxU).first()
    userR.index = FindIdxU
    userR.recipe_name = newRespNameU
    userR.rating = newRatingU
    userR.ingredients = newIngredientsU
    userR.servings = newServingsU
    userR.nutrition = newNutritionU
    userR.timing = newTimingU
    userR.directions = newDirectionsU

    db.session.commit()
    return redirect("/recipeU")

############################################################################################################

@recipeApp.route("/recipeA/delete", methods=["POST"])
def deleteRecipeA():
    delete_RecipeA = request.form.get("delete_RecipeA")
    admin = recipeClass.query.filter_by(index=delete_RecipeA).first()
    db.session.delete(admin)
    db.session.commit()
    return redirect("/recipeA")

@recipeApp.route("/recipeU/delete", methods=["POST"])
def deleteRecipeU():
    delete_RecipeU = request.form.get("delete_RecipeU")
    userR = recipeClass.query.filter_by(index=delete_RecipeU).first()
    db.session.delete(userR)
    db.session.commit()
    return redirect("/recipeU")

if __name__ == "__main__":
    recipeApp.run()