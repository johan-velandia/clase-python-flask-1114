
from flask import Flask, render_template



app = Flask(__name__)


@app.route("/")
def inicio():
     # Datos del portal
    nombre_profesor = "Prof. Henry - Kyrbot Innovations"
    email_profesor = "henry@kyrbot.com"
    horario = "Miercoles 16:45-18:10 | Jueves 12:30-14:20"
    aula = "215"
    descripcion = "Aprenderemos Python, Flask y construiremos un portal web real"

    return render_template(
        "index.html",
        profesor=nombre_profesor,
        email=email_profesor,
        horario=horario,
        aula=aula,
        descripcion=descripcion
    )

if __name__ == "__main__":

    app.run(debug=True)
