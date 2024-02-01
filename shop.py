item_taken = input("enter item taken: ")
item_taken_qty = int(input("enter item taken qty: "))
item_taken_price = int(input("enter item taken price: "))
print(item_taken)
print(item_taken_qty)
print(item_taken_price)
amount_paid = item_taken_price * item_taken_qty
print(f"amount to pay is {amount_paid} ")
