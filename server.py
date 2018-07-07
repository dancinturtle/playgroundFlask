from flask import Flask, render_template
app = Flask(__name__)
print(app)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/play")
def blueboxes():
    return render_template("joe.html", color="blue", number=3)
@app.route("/play/<x>")
def manyboxes(x):
    return render_template("joe.html", number=int(x), color="blue" )
@app.route("/play/<number>/<color>")
def variablecolor(number, color):
    return render_template("joe.html", number=int(number), color=color)




if __name__ == "__main__":
    app.run(debug=True)