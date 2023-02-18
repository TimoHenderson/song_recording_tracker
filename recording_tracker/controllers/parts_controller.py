from flask import Blueprint, render_template, request, redirect
from repositories import part_repository
from models.part import Part


parts_blueprint = Blueprint("parts", __name__)

# View all
@parts_blueprint.route("/parts")
def show_all():
    parts = part_repository.select_all()
    return render_template("parts/index.html", parts=parts)
