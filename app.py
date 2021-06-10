from flask import Flask, render_template, request, jsonify
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from models import db, Contact

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:picachu2171@localhost:3306/todolistft9'
db.init_app(app)
Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand) # db init, db migrate, db upgrade


@app.route("/")
def main():
    return render_template('index.html')

#@app.route('/api/contacts', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/api/contacts', methods=['GET', 'POST'])
@app.route('/api/contacts/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def contacts(id = None):
    if request.method == 'GET':
        if id is not None:
            contact = Contact.query.get(id)
            if contact:
                return jsonify(contact.serialize()), 200
            else:
                return jsonify({"msg": "Contact not found"}), 404    
        else:
            contacts = Contact.query.all()
            contacts = list(map(lambda contact: contact.serialize(), contacts))
        
        return jsonify(contacts),200
    if request.method == 'POST':
        name = request.json.get('name')
        phone = request.json.get('phone')
        address = request.json.get('address')

        contact = Contact()
        contact.name = name
        contact.phone = phone
        contact.address = address
        contact.save()

        return jsonify(contact.serialize()), 201
    if request.method == 'PUT':
        name = request.json.get('name')
        phone = request.json.get('phone')
        address = request.json.get('address')

        contact = Contact.query.get(id)

        if not contact:
             return jsonify({"msg": "Contact not found"}), 404

        contact.name = name
        contact.phone = phone
        contact.address = address
        contact.update()

        return jsonify(contact.serialize()), 200 
    if request.method == 'DELETE':
        contact = Contact.query.get(id)

        if not contact:
                return jsonify({"msg": "Contact not found"}), 404
        contact.delete()

        return jsonify({"result": "ok"}),200


    
if __name__ == '__main__':
    manager.run()