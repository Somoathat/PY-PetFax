from flask import Flask 

def create_app(): 
    app = Flask(__name__)

    @app.route('/')
    def index(): 
        return 'Hello, PetFax!'
    
 # register pet blueprint 
    from . import pet
    app.register_blueprint(pet.bp)
    app.register_blueprint(pet.bp_facts)
    return app


