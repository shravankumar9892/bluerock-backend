from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cat1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cat1 = db.Column(db.String(120))

class Cat2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cat2 = db.Column(db.String(120))
    id_cat1 = db.Column(db.Integer, db.ForeignKey('cat1.id'))

class Cat3(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cat3 = db.Column(db.String(120))
    id_cat1 = db.Column(db.Integer, db.ForeignKey('cat1.id'))
    id_cat2 = db.Column(db.Integer, db.ForeignKey('cat2.id'))

class Cat4(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cat4 = db.Column(db.String(120))
    id_cat1 = db.Column(db.Integer, db.ForeignKey('cat1.id'))
    id_cat2 = db.Column(db.Integer, db.ForeignKey('cat2.id'))
    id_cat3 = db.Column(db.Integer, db.ForeignKey('cat3.id'))

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    description = db.Column(db.String(120))
    price = db.Column(db.Integer)
    discount = db.Column(db.Integer)
    image = db.Column(db.String(120))
    id_cat4 = db.Column(db.Integer, db.ForeignKey('cat4.id'))