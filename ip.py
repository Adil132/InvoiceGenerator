def generate_invoice(invoice_no, customer_name, items, tax=18, discount=0):
    subtotal = 0

    print("\n========== INVOICE ==========")
    print("Invoice No:", invoice_no)
    print("Customer:", customer_name)
    print("-----------------------------")
    print("Product\t\tQty\tPrice\tAmount")

    for item in items:
        product = item["product"]
        quantity = item["quantity"]
        price = item["price"]

        amount = quantity * price
        subtotal += amount

        print(f"{product}\t\t{quantity}\t{price}\t{amount}")

    tax_amount = subtotal * tax / 100
    discount_amount = subtotal * discount / 100
    final_total = subtotal + tax_amount - discount_amount

    print("-----------------------------")
    print("Subtotal:", subtotal)
    print("Tax:", tax_amount)
    print("Discount:", discount_amount)
    print("Final Total:", final_total)
    print("=============================")


# Example
items = [
    {"product": "Laptop", "quantity": 2, "price": 50000},
    {"product": "Mouse", "quantity": 2, "price": 500},
    {"product": "Keyboard", "quantity": 1, "price": 1000}
]

generate_invoice(1001, "Adil", items, 18, 5)
