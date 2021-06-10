from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Contact(db.Model):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(100), nullable = False)
    phone = db.Column(db.String(100), nullable = False)
    address = db.Column(db.String(100), nullable = False)

    def serialize(self):
        return{
            "id":self.id,
            "name":self.name,
            "phone":self.phone,
            "address":self.address
        }


    def save(self):
        db.session.add(self)
        db.session.commit()  

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()