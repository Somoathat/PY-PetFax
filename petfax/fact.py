from flask import ( Blueprint, render_template, request, redirect) 

bp = Blueprint('fact', __name__, url_prefix="/facts")

@bp.route('/', methods=['GET', 'POST'])
def index():
    return 'Hello, Facts!'

    if request.method == 'POST':
        print("bp facts POST method")
    elif request.method == 'GET':
        print("bp facts get method")
        print(request.form)
        return redirect('/')
