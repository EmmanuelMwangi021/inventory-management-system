import requests

def get_product_by_barcode(barcode):
    url = f"https://world.openfoodfacts.org/api/v3/product/{barcode}"
    headers = {"User-Agent": "InventoryManagementSystem/1.0"}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return None
    
    data = response.json()
    product = data.get("product")
    if not product:
        return None
    
    return{
        "name": product.get("product_name"),
        "barcode": product.get("code"),
        "brand": product.get("brands")
    }

    