# catalog_microservice/routes.py
from flask import Blueprint, request, jsonify
from .models import db, Product

catalog_bp = Blueprint('catalog', __name__)

@catalog_bp.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    product_list = [{'id': product.id, 'name': product.name, 'price': product.price} for product in products]
    return jsonify({'products': product_list})

@catalog_bp.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    new_product = Product(name=data['name'], description=data.get('description'), price=data['price'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product created successfully'}), 201

# user_microservice/routes.py
from flask import Blueprint, request, jsonify
from .models import db, User

user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]
    return jsonify({'users': user_list})

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

# order_microservice/routes.py
from flask import Blueprint, request, jsonify
from .models import db, Order

order_bp = Blueprint('order', __name__)

@order_bp.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    order_list = [{'id': order.id, 'user_id': order.user_id, 'product_id': order.product_id, 'quantity': order.quantity} for order in orders]
    return jsonify({'orders': order_list})

@order_bp.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    new_order = Order(user_id=data['user_id'], product_id=data['product_id'], quantity=data['quantity'])
    db.session.add(new_order)
    db.session.commit()
    return jsonify({'message': 'Order created successfully'}), 201

