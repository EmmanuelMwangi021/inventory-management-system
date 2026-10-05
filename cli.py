from data.data import products
from services.openfoodfacts import get_product_by_barcode

def show_menu():
    print("\n=== Inventory Management System ===")
    print("1. List Products")
    print("2. Get Product")
    print("3. Add Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Search for Products using Barcode")
    print("7. Exit")

def list_products():
    for product in products:
        print(product)

def get_product():
    product_id = int(input("Enter product ID:"))
    for product in products:
        if product["id"] == product_id:
            print(product)
            break
    else:
        print("Product not found")

def add_product():
    name = input("Enter product name:")
    price = float(input("Enter product price:"))
    barcode = input("Enter product barcode:")
    quantity = int(input("Enter product quantity:"))

    new_id = max(product["id"] for product in products) + 1
    new_product = {
        "id": new_id,
        "name": name,
        "price": price,
        "barcode": barcode,
        "quantity": quantity
    }
    products.append(new_product)
    print("Product added successfully")

def update_product():
    product_id = int(input("Enter product ID to update:"))
    for product in products:
        if product["id"] == product_id:
            product["name"] = input(f"Enter new name:")
            product["price"] = float(input(f"Enter new price:"))
            product["quantity"] = int(input(f"Enter new quantity:"))

            print("Product updated successfully")
            break
    else:
        print("Product not found")

def delete_product():
    product_id = int(input("Enter product ID to delete:"))
    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            print("Product deleted successfully")
            break
    else:
        print("Product not found")

def search_product_by_barcode():
    barcode = input("Enter product barcode to search:")
    product = get_product_by_barcode(barcode)
    if product:
        print(product)
    else:
        print("Product not found!")

if __name__ == "__main__":
    while True:
        show_menu()

        choice = input("Choose an option:")

        if choice == "1":
            list_products()

        elif choice == "2":
            get_product()
        
        elif choice == "3":
            add_product()
        
        elif choice == "4":
            update_product()
        
        elif choice == "5":
            delete_product()
        
        elif choice == "6":
            search_product_by_barcode()
        
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option")
