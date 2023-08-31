#############################################################
#
# 1. Criar ambiente virtual Windows
#
# py -m venv .venv
# .venv\Scripts\activate
#
# 2. Instalar módulos Python
#
# pip install flask flask_mysqldb mysql-connector-python
#
# 3. Criar arquivo de requerimentos do projeto
#
# pip freeze > requirements.txt
#
#############################################################


from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import mysql.connector


app = Flask(__name__)

app.config['MYSQL_USER'] = 'tux'
app.config['MYSQL_PASSWORD'] = 'Mud@r123'
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_DB'] = 'banco'

app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql2 = MySQL(app)


# Página principal da aplicação usando arquivo "formulario.html"
@app.route('/',  methods=['GET','POST'])
def homepage():
    if request.method == 'POST':
        req = request.form        

        nome = req['nome']
        email = req.get('email')
        senha = request.form['senha']

        # print(f"\nNome: {nome}\nE-mail: {email}\nSenha: {senha}\n")
        if nome != "" and email != "" and senha != "":
            inserir(nome, email, senha)
        return redirect(request.url)		
    return render_template('formulario.html')


# Página de consulta ao Banco de dados
@app.route('/consultas')
def select():
    cur = mysql2.connection.cursor()
    cur.execute('''SELECT * FROM tbl_dados ORDER BY id ASC''')
    results = cur.fetchall()       
    return render_template("index.html", len = len(results), results = results) 


def inserir(nome, email, senha):
    comando = f'INSERT INTO tbl_dados (nome, email, senha) VALUES ("{nome}", "{email}", "{senha}")'

    conexao = mysql.connector.connect(
            host = '127.0.0.1',
            user = 'tux',
            password = 'Mud@r123',
            database = 'banco'
    )    
    cursor = conexao.cursor()
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()
  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
