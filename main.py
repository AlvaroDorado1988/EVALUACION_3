from livereload import Server
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    if request.method == "POST":
        nota1 = float(request.form["nota1"])
        nota2 = float(request.form["nota2"])
        nota3 = float(request.form["nota3"])
        asistencia = float(request.form["asistencia"])

        promedio = (nota1 + nota2 + nota3) / 3
        aprobado = promedio >= 40 and asistencia >= 75

        return render_template(
            "ejercicio_1.html",
            promedio=promedio,
            aprobado=aprobado
        )

    return render_template("ejercicio_1.html")

@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    if request.method == "POST":
        nombres = [
            request.form["nombre1"].strip(),
            request.form["nombre2"].strip(),
            request.form["nombre3"].strip()
        ]

        largos = [len(nombre) for nombre in nombres]
        largo_maximo = max(largos)

        nombres_ganadores = [
            nombre for nombre in nombres
            if len(nombre) == largo_maximo
        ]

        return render_template(
            "ejercicio_2.html",
            nombres_ganadores=nombres_ganadores,
            cantidad=largo_maximo
        )

    return render_template(
        "ejercicio_2.html",
        nombres_ganadores=None,
        cantidad=None
    )


if __name__ == "__main__":
    app.debug = True
    server = Server(app.wsgi_app)
    server.watch("templates/*.html")
    server.watch("static/*.css")
    server.serve(host="127.0.0.1", port=5001)
    
