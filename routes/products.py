from flask import jsonify, Blueprint, request
from models.product import products

products_blueprint = Blueprint("products", __name__)

# Route for getting all products
@products_blueprint.route("/api/products", methods=['GET'])
def get_products():
    return jsonify(products), 200

# Route for getting a single product by ID
@products_blueprint.route("/api/products/<int:product_id>", methods=['GET'])
def get_one_product(product_id):
    for product in products:
        if product["id"] == product_id:
            return jsonify(product)

    return jsonify({"error": "Product not found"}), 404

# Route for adding a new product
@products_blueprint.route("/api/products", methods=['POST'])
def add_product():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required for us to proceed"}), 400

    required_fields = ["name", "price", "quantity"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    new_product = {
        "id": len(products) +1,
        "name": data.get("name"),
        "barcode": data.get("barcode"),
        "price": data.get("price"),
        "quantity": data.get("quantity")
    }

    products.append(new_product)
    return jsonify(new_product), 201