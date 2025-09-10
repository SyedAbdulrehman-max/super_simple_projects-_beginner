user_choice=int(input("1.Add new expense\n2.Show all expense\n3.Show total spending\n4.Exit  (1/2/3/4)"))

def Expense_tracker():
    while True:
        if user_choice not in [1,2,3,4]:
            print("INVILD CHOICE")

        elif user_choice == 1:
            adding = input('Enter your expense: ')
            with open("Expense_tracker.txt",'a') as f:
                f.write(f'\n{adding}')

        elif user_choice == 2:
            with open("Expense_tracker.txt",'r') as f:
                print('Here is all expense!.\n')
                print(f.read())
            
        elif user_choice == 3:
            amount = []
            with open("Expense_tracker.txt",'r') as f:
                lines = f.readlines()

                for line in lines:
                    parts = f.strip().split('-')
                    amount = int(parts[1].strip())
                    amount.append(amount)
                total = sum(amount)
                print("Total spending:", total) 
        else:
            print("Have a good day")
            break
        
Expense_tracker()