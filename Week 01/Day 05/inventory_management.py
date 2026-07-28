#Mini Project 2 – Inventory Management System

products = [
    {
        "name": "Laptop",
        "price": 150000,
        "quantity": 10
    },
    {
        "name": "Mouse",
        "price": 500,
        "quantity": 50
    },
    {
        "name": "Keyboard",
        "price": 800,
        "quantity": 20
    },
    {
        "name" : "SSD",
        "price" : 2000,
        "quantity" : 30
    }
]

def add_product():
    name = str(input("Enter the name:"))
    price = input("Enter the price:")
    quantity = input("Enter the quantity:")
    product = {
        "name" : name,
        "price" : price,
        "quantity" : quantity
    }
    products.append(product)
    print("Product successfully Added.")
    print()
def view_product():
    for product in products:
        print(product)
        print()
def update_product():
    name = input("Enter the name of the product:")
    price = int(input("Enter the new price:"))
    quantity = int(input("Enter the quantity:"))
    for product in products:
        if name == product["name"]:
            product["price"] = price
            product["quantity"] = quantity
            print("Product successfully Updated.")
            print()
def delete_product():
    del_name = input("Enter the name of the product you want to delete:")
    for product in products:
        if product["name"] == del_name:
            products.remove(product)
            print("Product successfully Deleted.")
            print()
        else:
            print("No such Product found.")
            print()
def search_product():
    search_name = input("Enter the name:")
    for product in products:
        if product["name"] == search_name:
            print(product)
            print()
            return
    print("The name does not exist in the products.")
    print()

while True:
    print("    Inventory Management System      ")
    print()
    print("1.Add Product")
    print("2.View Products")
    print("3.Search Product")
    print("4.Update Product")
    print("5.Delete Product")
    print("6.Exit")
    print()

    choice = int(input("Enter your choice:"))
    print()
    if choice == 1:
        add_product()
    elif choice == 2:
        view_product()
    elif choice == 3:
        search_product()
    elif choice == 4:
        update_product()
    elif choice == 5:
        delete_product()
    elif choice == 6:
         print("Thankyou for using Inventory.")
         break
    else:
            print("Wrong Choice.")