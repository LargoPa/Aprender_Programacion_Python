
from flask import Flask, render_template, jsonify, request
from database.connectDB import get_connection
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
db = get_connection()


@app.route('/api/customers/<int:id>')
@cross_origin()
def getCustomer(id):
    try:
        cur = db.cursor()  # Crea el cursor
        cur.execute('SELECT id, firstname, lastname, email, phone, address FROM customers WHERE id='+str(id))
        data = cur.fetchall()
        cur.close()  # Cierra el cursor
        if not data:
            raise Exception("Cliente no encontrado")  # Levanta una excepción personalizada
        for row in data:
            return jsonify({'id': row[0], 'firstname': row[1], 'lastname': row[2], 'email': row[3], 'phone': row[4], 'address': row[5].decode('utf-8')})
    except Exception as e:
        return str(e)

@app.route('/api/customers')
@cross_origin()
def getAllCustomers():
    try:
        cur = db.cursor()  # Crea el cursor
        cur.execute('SELECT id, firstname, lastname, email, phone, address FROM customers')
        data = cur.fetchall()
        cur.close()  # Cierra el cursor
        if not data:  # Si no hay datos en la base de datos
            raise Exception("No hay datos en la base de datos")  # Levanta una excepción personalizada
        result = []
        for row in data:
            content = {'id': row[0], 'firstname': row[1], 'lastname': row[2], 'email': row[3], 'phone': row[4], 'address': row[5].decode('utf-8')}
            result.append(content)
        return jsonify(result)  # Devuelve los datos consultados
    except Exception as e:
        return str(e)


@app.route('/api/customers', methods=['POST'])
@cross_origin()
def createCustomer():
    try:
        firstname = request.json['firstname']
        lastname = request.json['lastname']
        email = request.json['email']
        phone = request.json['phone']
        address = request.json['address']
        if firstname and lastname and email and phone and address:
            cur = db.cursor()
            data = (firstname,lastname,email,phone,address)
            sql = ("INSERT INTO `customers` (`firstname`, `lastname`, `email`, `phone`, `address`) VALUES (%s,%s,%s,%s,%s);")
            cur.execute(sql, data)
            db.commit()
            cur.close()
            return "Cliente guardado"
    except Exception as e:
        return str(e)  # Devuelve el mensaje de error como respuesta


@app.route('/api/customers/<int:id>', methods=['PUT'])
@cross_origin()
def editCustomer(id):
    try:
        firstname = request.json['firstname']
        lastname = request.json['lastname']
        email = request.json['email']
        phone = request.json['phone']
        address = request.json['address']
        if firstname and lastname and email and phone and address:
            cur = db.cursor()
            data = (firstname,lastname,email,phone,address,id)
            sql = ("UPDATE `customers` SET firstname=%s, lastname=%s, email=%s, phone=%s, address=%s WHERE id=%s;")
            cur.execute(sql, data)
            db.commit()
            cur.close()
            return "Cliente editado"
    except Exception as e:
        return str(e)  # Devuelve el mensaje de error como respuesta


@app.route('/api/customers/<int:id>', methods=['DELETE'])
@cross_origin()
def removeCustomer(id):
    cur = db.cursor()
    cur.execute("DELETE FROM customers WHERE `customers`.`id` = "+str(id)+";")
    db.commit()
    return "Cliente eliminado"


@app.route('/')
@cross_origin()
def index():
    return render_template('index.html')


@app.route('/<path:path>')
@cross_origin()
def publicFiles(path):
    return render_template(path)


if __name__ == '__main__':
    app.run(debug=True, port=3000)

