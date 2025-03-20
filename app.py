# python.exe -m venv .venv
# cd .venv/Scripts
# activate.bat
# py -m ensurepip --upgrade
# pip install -r requirements.txt

from flask import Flask, render_template
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# Función centralizada para obtener la conexión a la base de datos
def get_db_connection():
    return mysql.connector.connect(
        host="185.232.14.52",
        database="u760464709_23005014_bd",
        user="u760464709_23005014_usr",
        password="B|7k3UPs3&P"
    )

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/app")
def app2():
    return "<h5>Hola, soy la view app</h5> <br> <h1>Do You Really Think I Need All Of These Guards In The HexGates</h1>"

@app.route("/trajes")
def trajes():
    con = get_db_connection()
    cursor = con.cursor(dictionary=True)

    sql = """
        SELECT IdTraje, Nombre, Descripcion
        FROM trajes
        LIMIT 10 OFFSET 0
    """

    cursor.execute(sql)
    registros = cursor.fetchall()

    cursor.close()
    con.close()

    return render_template("trajes.html", trajes=registros)  

@app.route("/rentas")
def rentas():
    con = get_db_connection()
    cursor = con.cursor(dictionary=True)

    sql = """
        SELECT rentas.*, trajes.Nombre, trajes.Descripcion 
        FROM rentas
        INNER JOIN trajes ON trajes.IdTraje = rentas.IdTraje
        LIMIT 10 OFFSET 0
    """

    cursor.execute(sql)
    registros = cursor.fetchall()

    cursor.close()
    con.close()

    return render_template("rentas.html", rentas=registros)

# Ejecutar la aplicación una sola vez
if __name__ == "__main__":
    app.run(debug=True)
