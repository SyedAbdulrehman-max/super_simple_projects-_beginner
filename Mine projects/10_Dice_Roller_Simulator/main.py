import random 

def roll_dice():

    while True:
        #Start and stop 
        s_or_e =(input("1.START\t2.STOP\nChoice (1/2): "))

        #choice the number of dice

        #condition no1

        if s_or_e == '1':
            choice_dice = int(input("Enter the number of dice(1/2): "))
            print('')

            #ONE DICE ROLL

            if choice_dice == 1:
                n1= print(f"The one dice number is {random.randint(1,6)}")
                ask1 = input("Want to play again!(y/n):").lower()

                if ask1 == 'y':
                    continue
                elif ask == 'n':
                    print("Thanks for playing...!")
                    break

            elif s_or_e != 1 and s_or_e != 2:
                print("Please enter vaild number")
                continue

            #TWO DICE ROLL

            elif choice_dice == 2:
                n2 =print(f"The two dice number are {random.randint(1,6)} and {random.randint(1,6)}")
                print(' ')
                ask = input("Want to play again!(y/n):").lower()
                print('')

                if ask == 'y':
                    continue
                elif ask=='n':
                    print("Thanks for playing...!")
                    break

        #condition no2 of choice the number of dice

        elif s_or_e == '2':
            print("Thanks for playing...!")
            break
        
     #condition no3 of choice the number of dice

        elif s_or_e != 1 and s_or_e != 2:
            print("Please enter vaild number")
            continue

roll_dice()

                
