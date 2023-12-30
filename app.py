from flask import Flask, request, jsonify
from models import db, Product

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///catalog.db'
db.init_app(app)

@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    product_list = [{'id': product.id, 'name': product.name, 'price': product.price} for product in products]
    return jsonify({'products': product_list})

@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    new_product = Product(name=data['name'], description=data.get('description'), price=data['price'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product created successfully'}), 201
