def payment():
    customer = int(input("Enter your bill: "))

    tip_percentage = int(input("Enter the tip percentage: "))
    tip = (tip_percentage/100)*customer

    total_bill =  int(customer+tip)
    while True:
        pay_bill = (input("1.Pay bill\n2.Buy more(1/2): "))

        if pay_bill != "1" and pay_bill != "2":
            print("Invild option..! Please choice correct option")
            continue

        elif pay_bill == "1":
            print(f"Your total bill is {total_bill} has been paid")
            break

        elif pay_bill == "2" :
            print("Pizza: 100rs , Burger: 300rs")
            ex=int(input("Enter your item pirce: "))
            print(f"Now your total price is {round(total_bill+ex,2)}")
            continue


payment()
print("Thanks for choicing us:)")
