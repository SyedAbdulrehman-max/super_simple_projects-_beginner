def calculator():
    while True:
        print("Choice opretion\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.EXIT")
        user = int(input("Enter the opration: "))
        if user == 5:
            print("Thanks for using our calculater")
            break
        if user not in [1,2,3,4]:
            print("Invild choice")
            continue

        n1= int(input("Enter the first number: "))
        n2=int(input("Enter the Second number: "))

        if user == 1:
            print(f"The sum of {n1} and {n2} = {n1+n2}")
        elif user == 2:
            print(f"The subtraction of {n1} and {n2} = {n1-n2}")
        elif user == 3:
            print(f"The multiplycation of {n1} and {n2} = {n1*n2}")
        elif user == 4:
            if n2 != 0:
                print(f"The division of {n1} and {n2} = {n1 / n2}")
            else:
                print("Error: Division by zero is not allow")
calculator()