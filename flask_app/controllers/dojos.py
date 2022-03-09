from flask import render_template, request, redirect 
from flask_app.models.dojo import Dojo
from flask_app import app


@app.route('/')
def index():
    return render_template("form.html")

@app.route('/create', methods=["POST"])
def create_dojo():
    if not Dojo.validate_dojo(request.form):
        return redirect('/')
    Dojo.save(request.form)
    return redirect("/show")


@app.route('/show')
def show_dojo():
    Dojo.get_one(request.form)
    return render_template("result.html")