from flask import (Blueprint, render_template, send_from_directory, request, redirect)
import json

pets= json.load(open('pets.json'))
print(pets)

bp = Blueprint('pet', __name__, url_prefix="/pets")
# bp_facts = Blueprint('fact', __name__, url_prefix="/facts")
# bp.register_blueprint(bp_facts)

@bp.route('/')
def index(): 
    return render_template('index.html', pets=pets)

@bp.route('/<pet_number>')
def single_pet(pet_number):  # each function name has to be unique

    # Show information for pet_id = pet_number....
    # Find the pet in pets where pet_id = pet_number
    # Loop through pets
    # for VARNAME in COLLECTION:
    for the_pet in pets:
        # See if pet_id == pet_number
        if the_pet['pet_id'] == int(pet_number):
            return render_template('single_pet.html', PET=the_pet)
    return "<p>No pet number " + pet_number + " found. :( </p>"


#@bp_facts.route("/", methods=['GET'])
#def new_facts():
#    return send_from_directory('static',"new_facts.html")
