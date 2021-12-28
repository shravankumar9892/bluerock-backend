import os
from flask import Flask, json, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import Cat1, Cat2, Cat3, Cat4, Products, db

# creating a Flask app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://{0}:{1}@{2}/bluerock_products".format("root", os.environ.get('PASSWORD_DATABASE'), "localhost:3306")
db.init_app(app)


"""
Returns products depending on the metadata and value
Returns values from the Products table

JSON body
{
    metadata: 'cat4' | 'title' | 'all' # literal strings
    value: 'cat4' | 'title' | '' # replaced by corresponding values
}
"""
@app.route('/products', methods = ['POST'])
def products():
    if (request.method == 'POST'):
        data = request.get_json()
        if (data["metadata"] == 'cat4'):
            id_cat4 = Cat4.query.filter_by(cat4 = data["value"]).first().id
            products = Products.query.filter_by(id_cat4=id_cat4).all()

            decoded_products = []
            for product in products:
                decoded_products.append({
                    "id": product.id,
                    "title": product.title,
                    "price": product.price,
                    "discount": product.discount,
                    "description": product.description,
                    "image": product.image
                })
            return jsonify(decoded_products)
        elif (data["metadata"] == 'title'):
            product = Products.query.filter_by(title=data["value"]).first()
            response = {
                "id": product.id,
                "title": product.title,
                "price": product.price,
                "discount": product.discount,
                "description": product.description,
                "image": product.image
            }
            return jsonify(response)
        elif (data["metadata"] == 'all'):
            products = Products.query.all()
            decoded_products = []
            for product in products:
                decoded_products.append({
                    "id": product.id,
                    "title": product.title,
                    "price": product.price,
                    "discount": product.discount,
                    "description": product.description,
                    "image": product.image
                })
            return jsonify(decoded_products)
    elif (request.method == 'GET'):
        return "GET response working"

if __name__ == '__main__':
    app.run(port=5000, debug = True)