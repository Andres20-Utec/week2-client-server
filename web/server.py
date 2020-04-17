from flask import Flask,render_template, request, session, Response, redirect
from database import connector
from model import entities
import math
import json
import time
#import math

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)


@app.route('/espar/<numero>')
def par(numero):
    return str(int(numero) % 2 == 0)

@app.errorhandler(404)
def page_not_found(e):
    return "NOT FOUND XD", 404

@app.route('/esprimo/<numero>')
def es_primo(numero):
    # Acortamos el rango de busqueda
    num = int(numero)
    youtubeFormula = math.ceil(math.sqrt(num))
    for i in range(2, youtubeFormula+1):
        if(num%i==0 and i!=num):# Buscamos multiplos
            return str(False)
    if(num<2):
        return str(False)
    else:
        return str(True)


@app.route('/saludar')
def saludar():
    return "Hola2"
# <content> es una (variable = html/hello.html)

@app.route('/static/<content>') 
def static_content(content):
    return render_template(content)

if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))
