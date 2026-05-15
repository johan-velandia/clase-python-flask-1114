
from flask import Flask, render_template



app = Flask(__name__)



@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/hola")
def hola():
    return render_template("hola.html")

@app.route("/ola")
def ola():
    return render_template("ola.html")

@app.route("/trabajo")
def trabajo():
    return render_template("trabajo.html")

@app.route("/eu")
def eu():
    return render_template("eu.html")

@app.route("/acerca")
def acerca():
    return render_template("acerca.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")












if __name__ == "__main__":
    app.run(debug=True)


