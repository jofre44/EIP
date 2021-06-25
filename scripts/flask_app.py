from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    
    to_show = """<h1>Hola mundo con Flask </h1>
                 <p>Actividad 10. Programacion Avanzada en Python </p>
                 <p>Alumno: Jose Sepulveda </p>"""

    return to_show

if __name__ == "__main__":
    app.run(host = '127.0.0.1', port=8080, debug=True)