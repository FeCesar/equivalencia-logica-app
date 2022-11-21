from flask import *
from expressions import get_logical_equivalences_by
from expressions import get_all
from table import generate_truth_table

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if(request.method == "POST"):
        expression = request.form["expression"]
        return render_template("results.html", results=get_logical_equivalences_by(expression))

    return render_template("index.html")

@app.route('/all', methods=["GET"])
def all():
    return render_template("all.html", all=get_all())

@app.route('/tabela-verdade', methods=["GET", "POST"])
def tabela():
    if(request.method == "POST"):
        return render_template("tabela-resultados.html", resultado=generate_truth_table(request.form))

    return render_template("tabela.html")