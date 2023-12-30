# app.py
from flask import Flask
from config import DevelopmentConfig
from catalog_microservice.routes import catalog_bp
from user_microservice.routes import user_bp
from order_microservice.routes import order_bp
from catalog_microservice.models import db as catalog_db
from user_microservice.models import db as user_db
from order_microservice.models import db as order_db

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

app.register_blueprint(catalog_bp, url_prefix='/catalog')
app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(order_bp, url_prefix='/order')

catalog_db.init_app(app)
user_db.init_app(app)
order_db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        catalog_db.create_all()
        user_db.create_all()
        order_db.create_all()
    app.run(debug=True)
