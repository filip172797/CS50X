due = 50
while True:
    print("Amount Due:", due)
    payed = int(input("Insert Coin:"))
    if payed in [25, 10, 5]:
        due = due - payed
        if due <= 0:
            break
    
print("Change Owed:", -due)

