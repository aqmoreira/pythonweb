from flask import Flask, g
import sqlite3 #import para usar banco de dados

DATABASE = "blog.bd"    #dados do banco de ddos
SECRETE_KEY = "senhaForte" #senha


app = Flask(__name__) #app vai ser o nome do arquivo
app.config.from_object(__name__)    #local de onde busca as propriedade de config

def conectar_bd():  #função para conectar com banco de dados.
    return sqlite3.connect(DATABASE)

#Comando para criar o BD no terminal
# sqlite3 blog.bd < esquema.sql

@app.before_request
def antes_requisicao():     #funcao que vai rodar antes da requisicao
    g.bd = conectar_bd()

@app.teardown_request       #função que vai rodar após a requisiição
def fim_requisicao(exc):
    g.bd.close()



@app.route('/')
def exibir_entradas():
    sql = "SELECT titulo,texto FROM entradas ORDER BY id DESC"  #string sql de pesquisa no banco de dados
    cur = g.bd.execute(sql)  #executa o sql no banco de dados e salva o retorno em cur
    entradas = []
    return str(entradas)
    
    return "Hello from Flask"

#@app.route('/robopisca') #exemplo de outra url
#def robopisca():
#    return "#RoboPisca"

