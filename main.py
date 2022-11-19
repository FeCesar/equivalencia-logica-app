from flask import *
from expressions import get_logical_equivalences_by
from expressions import get_all

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if(request.method == "POST"):
        expression = request.form["expression"]
        return render_template("results.html", results=get_logical_equivalences_by(expression))

    return render_template("index.html")

@app.route('/referencias', methods=["GET"])
def referencias():
    return render_template("referencias.html")

@app.route('/all', methods=["GET"])
def all():
    return render_template("all.html", all=get_all())