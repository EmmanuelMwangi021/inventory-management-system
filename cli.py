def show_menu():
    print("\n=== Inventory Management System ===")
    print("1. List Products")
    print("2. Get Product")
    print("3. Add Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Search OpenFoodFacts")
    print("7. Exit")

if __name__ == "__main__":
    show_menu()

    choice = input("Choose an option:")

    if choice == "1":
        print("Listing products...")
    elif choice == "7":
        print("Goodbye!")
    else:
        print("Invalid option")

