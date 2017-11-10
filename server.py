from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninjas')
def ninjas():
    return render_template("ninjas.html")

@app.route('/dojo')
def dojoform():
    return render_template("dojo.html")

@app.route('/dojo/new', methods=["POST"])
def dojo():
    print request.form["name"]
    print request.form["hobby"]
    return "Thanks for the data!"



app.run(debug=True)
