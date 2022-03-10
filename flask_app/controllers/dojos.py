from flask import render_template, request, redirect 
from flask_app.models.dojo import Dojo
from flask_app import app


@app.route('/')
def index():
    return render_template("form.html")

# @app.route('/process', methods=["POST"])
# def create_dojo():
#     if Dojo.validate_dojo(request.form):
#         Dojo.save(request.form)
#         return redirect("/results")
#     return redirect("/")


# @app.route('/results')
# def show_dojo():
#     dojo = Dojo.get_one()
#     return render_template("result.html", dojo = dojo )



@app.route('/submit', methods=["POST"])
def submit():
    print(request.form)
    if not Dojo.is_valid(request.form):
        return redirect("/")
    data = {
    "name" : request.form["name"],
    "location" : request.form["location"],
    "language" : request.form["language"],
    "comment" : request.form["comment"]
    }
    new_dojo_id = Dojo.save(data)
    print(new_dojo_id)
    return redirect(f'/display/{new_dojo_id}',)

@app.route('/display/<int:id>')
def display(id):
    data = {
        "id": id
    }
    return render_template("results.html", dojo = Dojo.get_by_id(data))