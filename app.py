# python.exe -m venv .venv
# cd .venv/Scripts
# activate.bat
# py -m ensurepip --upgrade
# pip install -r requirements.txt

from flask import Flask, render_template
from flask_cors import CORS
import mysql.connector
import datetime
import pytz

app = Flask(__name__)
CORS(app)

# Establece la conexión de manera centralizada
def get_db_connection():
    return mysql.connector.connect(
        host="185.232.14.52",
        database="u760464709_23005014_bd",
        user="u760464709_23005014_usr",
        password="B|7k3UPs3&P"
    )

@app.route("/")
def index():
    con = get_db_connection()
    cursor = con.cursor(dictionary=True)

    # Puedes consultar lo que necesites en esta ruta
    cursor.close()
    con.close()

    return render_template("index.html")

@app.route("/app")
def app2():
    return "<h5>Hola, soy la view app</h5> <br> <h1>Do You Really Think I Need All Of These Guards In The HexGates</h1>"

@app.route("/rentas")
def trajes():
    con = get_db_connection()
    cursor = con.cursor(dictionary=True)
    sql = """
        SELECT IdTraje, Nombre, Descripcion
        FROM rentas
        LIMIT 10 OFFSET 0
    """

    cursor.execute(sql)
    registros = cursor.fetchall()

    cursor.close()
    con.close()

    return render_template("rentas.html", rentas=registros)

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/rentas")
def rentas():
    con = get_db_connection()
    cursor = con.cursor(dictionary=True)
    sql = """
        SELECT * FROM rentas
        INNER JOIN trajes ON trajes.IdTraje = rentas.IdTraje
        LIMIT 10 OFFSET 0
    """

    cursor.execute(sql)
    registros = cursor.fetchall()

    cursor.close()
    con.close()

    return render_template("rentas.html", rentas=registros)

if __name__ == "__main__":
    app.run(debug=True)
