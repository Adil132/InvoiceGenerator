def generate_invoice(customer_name, product, quantity, price):
    total = quantity * price

    print("----- INVOICE -----")
    print("Customer:", customer_name)
    print("Product:", product)
    print("Quantity:", quantity)
    print("Price:", price)
    print("Total:", total)
    print("-------------------")


# Example
generate_invoice("Adil", "Laptop", 2, 50000)
