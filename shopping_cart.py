print("\t=======ITEMS AVAILABLE========")

print("""
      1.bread\t2500
      2.sugar\t3500
      3.cooking oil 1500
      4.soap\t1000
       """)
item_code = int(input("enter itemcode: "))
item_qty = int(input("enter item qty: "))
item_price = 0
item_name = ""
discount = 0
final_pay=0

if item_code == 1:
    item_name = "bread"
    item_price = 2500*item_qty
elif item_code == 2:
    item_name = "sugar"
    item_price = 3500*item_qty
elif item_code == 3:
    item_name = "cooking oil"
    item_price = 1500*item_qty
elif item_code == 4:
    item_name = "soap"
    if item_qty >=10:
        discount = 0.05 * (1000*item_qty)
        final_pay = item_price - discount
    else:
        item_price = 1000*item_qty 
else:
    print("invalid input")

print(f"""item taken: {item_name}\n item price: {item_price}\n discount: {discount}\n total amount: {final_pay}  """ )