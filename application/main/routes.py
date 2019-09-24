from flask import request, jsonify, Blueprint, render_template
import json


main = Blueprint('main', __name__)

@main.route("/", methods=['GET', 'POST'])
def upload_file():
    return render_template("layout.html", title = "home")