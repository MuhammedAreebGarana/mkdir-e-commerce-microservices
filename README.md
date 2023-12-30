# mkdir-e-commerce-microservices
Microservice 1: Product Catalog Management

Objective:
The primary objective of this microservice is to handle the product catalog, allowing users to retrieve a list of products and add new products to the catalog.

Key Features:

Product Retrieval:

Endpoint: /products (GET)
Retrieves a list of products from the product catalog.
Product Creation:

Endpoint: /products (POST)
Allows users to add new products to the catalog by providing product details such as name, description, and price.
Technologies Used:

Backend Framework: Flask (Python)
Database: SQLAlchemy (SQLite for simplicity in the example)
Version Control: Git
Project Structure:

models.py: Defines the database model for the product catalog.
app.py: Main application file containing the Flask application and routes for product management.
venv/: Virtual environment for dependency management.
requirements.txt: Lists project dependencies.
