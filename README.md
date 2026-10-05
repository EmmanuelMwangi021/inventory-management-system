# inventory-management-system

A Python-based inventory management system built with Flask. The project provides a REST API for managing products and a command-line interface (CLI) for interacting with the inventory.

The application also integrates with the OpenFoodFacts API to search for product information using a barcode.

# Features

## REST API

- Get all products
- Get a single product by ID
- Add a new product
- Update an existing product
- Delete a product
- Search for a product using a barcode
- Search for products by name
- Input validation and error handling

## Command-Line Interface

The CLI allows users to:

1. List all products
2. Get a product by ID
3. Add a product
4. Update a product
5. Delete a product
6. Search for a product using a barcode
7. Exit the application

## OpenFoodFacts Integration

The application uses the OpenFoodFacts API to look up product information by barcode.

The API returns information such as:

- Product name
- Barcode
- Brand

## Technologies Used

- Python
- Flask
- Requests
- Pytest
- OpenFoodFacts API
- JSON

## Project Structure

inventory-management/
│
├── app.py
├── cli.py
├── requirements.txt
├── README.md
│
├── data/
│ └── data.py
│
├── routes/
│ └── products.py
│
├── services/
│ └── openfoodfacts.py
│
└── tests/
    ├── test_api.py
    ├── test_cli.py
    └── test_openfoodfacts_api.py



# Setup and Installation

1. Clone the repository

git clone <my-repository-url>
cd inventory-management

2. Create and activate a virtual environment

Using Python's built-in virtual environment:

python3 -m venv .venv

Activate it on Linux/macOS:

source .venv/bin/activate

On Windows:

.venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

## Running the Flask API

Start the Flask application with:

python3 app.py

The application will run locally and can be accessed at:

http://127.0.0.1:5000

The root endpoint returns:

Inventory Management System

## API Endpoints

Method| Endpoint| Description
GET| "/api/products"| Get all products
GET| "/api/products/<product_id>"| Get a product by ID
POST| "/api/products"| Add a new product
PATCH| "/api/products/<product_id>"| Update a product
DELETE| "/api/products/<product_id>"| Delete a product
GET| "/api/products/barcode/<barcode>"| Search OpenFoodFacts using a barcode
GET| "/api/products/search?name=<name>"| Search products by name

### Adding a Product

Send a "POST" request to:

/api/products

Example request body:

{
    "name": "Nutella",
    "price": 650,
    "quantity": 10,
    "barcode": "3017624010701"
}

### Updating a Product

Send a "PATCH" request to:

/api/products/<product_id>

Example:

{
    "price": 700,
    "quantity": 8
}

### Deleting a Product

Send a "DELETE" request to:

/api/products/<product_id>

The API returns a success message when the product is deleted.

# Command-Line Interface

Run the CLI with:

python cli.py

The CLI displays the following menu:

=== Inventory Management System ===
1. List Products
2. Get Product
3. Add Product
4. Update Product
5. Delete Product
6. Search for Products using Barcode
7. Exit

Select an option by entering its corresponding number.

# OpenFoodFacts API

The project uses the OpenFoodFacts API to retrieve product information using a barcode.

The external API is accessed through the service:

services/openfoodfacts.py

The application sends a request to OpenFoodFacts and extracts the product name, barcode, and brand from the response.

If the external API request fails or the product cannot be found, the application handles the situation and reports that the product was not found.

# Error Handling

The API validates incoming product data before adding or updating products.

Examples of validation include:

- Required fields must be provided when creating a product.
- Product names must contain text.
- Prices must be valid numbers.
- Quantities must be non-negative integers.
- Products that do not exist return a "404" response.
- Invalid request data returns a "400" response.

# Testing

The project uses pytest for automated testing.

Run all tests with:

pytest

The test suite covers:

- Flask API endpoints
- CLI functionality
- OpenFoodFacts API integration
- External API mocking


# Contributors

This project was developed by Emmanuel Mwangi.