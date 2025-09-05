while True:
    
    choice = int(input('''Choose conversion:
    1. Km → Miles
    2. Miles → Km
    3. Celsius → Fahrenheit
    4. Fahrenheit → Celsius
    5. EXIT
    Enter your choice (1-4): '''))
    
    #invild number if choice other number 

    if choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice !=5 :
        print("Invild Choice!!")
        continue

    # km →→→ Miles

    elif choice == 1:
        km = float(input("Enter the km: "))

        print(f"Result: {km} km  = {round(km * 0.621371, 2)} miles")
        continue

    # miles ---> km
    elif choice == 2:
        miles = float(input('Enter Miles: '))
        print(f"Restul: {miles} = {round(miles / 0.621371,2) } km ")
        continue
    # celsius (°C) → Fahrenheit (°F)

    elif choice == 3:
        celsius = int(input("Enter the celsius :"))
        print(f"Result: {celsius} c  = {(celsius * 9/5) + 32}")

        continue

    #Fahrenheti ---> Celsius

    elif choice == 4:

        fahrenheit = int(input("Enter Fahrenheit: "))

        print(f"{(fahrenheit - 32)*(5/9) }")

    #Exit
    
    else:
        print("Thanks for using converter!!")
        break