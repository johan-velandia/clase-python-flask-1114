# Importamos Flask y una funcion que permite mostrar un HTML.
from flask import Flask, render_template


# Creamos la aplicacion principal.
# Este objeto sera el centro de nuestro proyecto Flask.
app = Flask(__name__)


# Cuando alguien entra a la direccion principal del sitio, Flask ejecuta
# esta funcion y devuelve la pagina `index.html`.
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













if __name__ == "__main__":
    app.run(debug=True)


