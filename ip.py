def generate_invoice(invoice_no, customer_name, product, quantity, price, tax=0, discount=0):
    subtotal = quantity * price
    tax_amount = subtotal * tax / 100
    discount_amount = subtotal * discount / 100
    total = subtotal + tax_amount - discount_amount

    print("\n----- INVOICE -----")
    print("Invoice No:", invoice_no)
    print("Customer:", customer_name)
    print("Product:", product)
    print("Quantity:", quantity)
    print("Price:", price)
    print("Subtotal:", subtotal)
    print("Tax:", tax_amount)
    print("Discount:", discount_amount)
    print("Total:", total)
    print("-------------------")


# Example
generate_invoice(101, "Adil", "Laptop", 2, 50000, 18, 5)
