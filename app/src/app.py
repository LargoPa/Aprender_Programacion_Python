
from flask import Flask,render_template,request,redirect,url_for
import os
import database as db


template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir,'src','templates')


app = Flask(__name__)


@app.route('/')
def home():
    cur = db.database.cursor()
    cur.execute("SELECT * FROM users")
    resultado = cur.fetchall()
    #Convertir los datos a diccionario
    insertObject = []
    columnNames = [column[0] for column in cur.description]
    for record in resultado:
        insertObject.append(dict(zip(columnNames, record)))
    cur.close()
    return render_template('index.html', data=insertObject)


#ruta para guardar usuarios en la bd
@app.route('/user', methods=['POST'])
def addUser():
    username = request.form['username']
    name = request.form['name']
    password = request.form['password']
    if username and name and password:
        cur = db.database.cursor()
        sql= "INSERT INTO users (nombreUsuario, nombre, contrasenia) VALUES (%s, %s, %s);"
        data = (username,name,password)
        cur.execute(sql,data)
        db.database.commit()
        cur.close()
    return redirect(url_for('home'))


@app.route('/delete/<int:id>')
def delete(id):
    cur = db.database.cursor()
    cur.execute( f"DELETE FROM users WHERE id={id};")
    db.database.commit()
    cur.close()
    return redirect(url_for('home'))


@app.route('/edit/<int:id>', methods=['POST'])
def edit(id):
    username = request.form['username']
    name = request.form['name']
    password = request.form['password']
    if username and name and password:
        cur = db.database.cursor()
        sql= "UPDATE users SET nombreUsuario = %s, nombre=%s, contrasenia=%s WHERE id=%s;"
        data = (username,name,password,id)
        cur.execute(sql,data)
        db.database.commit()
        cur.close()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True, port=4000)
    



