# sending of money from one person to another.
current_balance = 50000
receipients_number= input("enter receipients number: ")
amount_to_send = int(input("enter amount to send: "))
pin_number = input("enter pin_number: ")
balance = current_balance - amount_to_send
# confirmation message
print  (f"you have sent {amount_to_send} to {receipients_number} and your account balance is {balance}")