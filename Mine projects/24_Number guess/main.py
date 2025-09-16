import random

while True:

    user_choice = int(input("1.Start the game\n2.Exit:  ")) 
    
    if user_choice not in [1,2]:
        print('invild choice !')

    elif user_choice == 2 :
        print('Thanks for playing')
        break

    elif user_choice == 1:
        computer  = random.randint(1,100)
        
        print('You have only five chances')
        
        count = 0

    while True:
        
            count += 1
            
            user = int(input('Guess the number: '))

            if count == 5:
                print('You lose ')
                print(f'The number was {computer}')
                break       

            if user < computer:
                print('Enter larger number !')
                

            elif user > computer :
                print('Enter smaller number !')
                

            elif user == computer:
                print('You Won!')
                break

        