from app import app

def test_get_products():
    client = app.test_client()
    response = client.get("/api/products")
    assert response.status_code == 200

def test_get_product():
    client = app.test_client()
    response = client.get("/api/products/1")
    assert response.status_code == 200

def test_create_product():
    client = app.test_client()
    response = client.post("/api/products", json={"name": "Juice", "price": 150, "barcode": "1112223334445", "quantity": 12})
    assert response.status_code == 201

def test_update_product():
    client = app.test_client()
    response = client.patch("/api/products/1", json={ "price": 200, "quantity": 15 })
    assert response.status_code == 200

def test_delete_product():
    client = app.test_client()
    response = client.delete("/api/products/1")
    assert response.status_code == 200

def test_get_product_not_found():
    client = app.test_client()
    response = client.get("/api/products/999")
    assert response.status_code == 404

def test_create_product_invalid_data():
    client = app.test_client()
    response = client.post("/api/products", json={"name": "", "price": -100, "barcode": "1112223334445", "quantity": 12})
    assert response.status_code == 400

def test_update_product_not_found():
    client = app.test_client()
    response = client.patch("/api/products/999", json={"price": 200})
    assert response.status_code == 404

def test_delete_product_not_found():
    client = app.test_client()
    response = client.delete("/api/products/999")
    assert response.status_code == 404