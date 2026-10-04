from flask import jsonify, Blueprint, request
from data.data import products

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
    
    if not isinstance(data["name"], str) or not data["name"].strip():
        return jsonify({"error": "Name must be text and cannot be empty"}), 400

    if not isinstance(data["price"], (int, float)) or data["price"] < 0:
        return jsonify({"error": "Price must be a positive number"}), 400
    
    if not isinstance(data["quantity"], int) or data["quantity"] < 0:
        return jsonify({"error": "Quantity must be a positive integer"}), 400



    new_product = {
        "id": len(products) +1,
        "name": data["name"].strip(),
        "barcode": data.get("barcode"),
        "price": data["price"],
        "quantity": data["quantity"]
    }

    products.append(new_product)
    return jsonify(new_product), 201


#Route for updating an existing product
@products_blueprint.route("/api/products/<int:product_id>", methods = ["PATCH"])
def update_product(product_id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400
    
    product = None
    for item in products:
        if item["id"] == product_id:
            product = item
            break
    
    if product is None:
        return jsonify({"error": "Product not found"}), 404

    #What fields is the user allowed to update? (cant update id)
    allowed_fields = ["name", "price", "quantity"]
    for field in data:
        if field not in allowed_fields:
            return jsonify({"error": f"{field}Cannot update Field"}), 400
    
    
    if "name" in data:
        if not isinstance(data["name"], str) or not data["name"].strip():
            return jsonify({
                "error": "Name must be text and cannot be empty."
            }), 400

    if "price" in data:
        if not isinstance(data["price"], (int, float)) or data["price"] <= 0:
            return jsonify({
                "error": "Price must be a number greater than 0."
            }), 400

    if "quantity" in data:
        if not isinstance(data["quantity"], int) or data["quantity"] < 0:
            return jsonify({
                "error": "Quantity must be a non-negative value."
            }), 400

    # Update the product with the new values
    if "name" in data:
        product["name"] = data["name"].strip()

    
    if "price" in data:
        product["price"] = data["price"]

    if "quantity" in data:
        product["quantity"] = data["quantity"]

    return jsonify(product)


# Route for deleting a product by ID
@products_blueprint.route("/api/products/<int:product_id>", methods = ["DELETE"])
def delete_product(product_id):
    product = None
    for item in products:
        if item["id"] == product_id:
            product = item
            break
        
        if product is None:
            return jsonify({"error": "Product not found"}), 404
        
        products.remove(product)
        return jsonify({"message": "Product deleted successfully."}), 200
