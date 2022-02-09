from flask import Flask
import sqlite3 #import para usar banco de dados

DATABASE = "blog.bd"    #dados do banco de ddos
SECRETE_KEY = "senhaForte" #senha

app = Flask(__name__) #app vai ser o nome do arquivo
app.config.from_object(__name__)    #local de onde busca as propriedade de config

def conectar_bd():  #função para conectar com banco de dados.
    return sqlite3.connect(DATABASE)

#Comando para criar o BD no terminal
# sqlite3 blog.bd < esquema.sql

@app.route('/')
@app.route('/home')
def home():
    return "Hello from Flask"

@app.route('/robopisca')
def robopisca():
    return "#RoboPisca"

