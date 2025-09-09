import random

count = 0
counts = 0
while True:

    #choice
    
    options = ['Rock','Paper','Scissors']
    
    #computer choice
    
    computer = random.choice(options).lower()
    
    #user choice
    
    user = input("Enter your choice\nRock , Paper or Scissors \nExit :) _\n").lower()
    
    #Exit
    
    if user == 'exit':
        print("Thanks for playing!!!")
        break
    
    #Display Choices
    
    print(f"you choice {user}")
    print(f'Computer choice {computer}')

    #invild Choice
    
    if user != 'rock' and user != 'paper' and user != 'scissors':
        print('Invild choice!..')
        
    #Tie
    
    elif user == computer:
        print('Its a tie...')

    #WOn

    elif (user == 'scissor' and computer == 'paper')or\
        (user == 'paper' and computer  == 'rock' ) or\
        (user == 'rock' and computer == 'scissor'):
        print('You won')
        counts += 1
        print(counts,'Times.')
    
    #Lose

    else:
        print('YOU LOSE')
        count += 1
        print(count)
        

