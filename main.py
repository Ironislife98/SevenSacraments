from flask import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("Index.html")

@app.route('/baptism')
def baptism():
    return render_template("baptism.html")

@app.route("/confirmation")
def confirmation():
    return render_template("confirmation.html")

@app.route("/eucharist")
def eucharist():
    return render_template("eucharist.html")

@app.route("/penance")
def penance():
    return render_template("penance.html")

@app.route("/anointing")
def anointing():
    return render_template("anointing.html")

@app.route("/holyorders")
def holyorders():
    return render_template("holyorders.html")

@app.route('/marriage')
def marriage():
    return render_template("marriage.html")
if __name__ == "__main__":
    app.run(debug=True)
