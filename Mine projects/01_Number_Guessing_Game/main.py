import random

computer = random.randint(1,100)
player = int(input("Guess the number"))

while computer !=player:
    if computer < player:
        print("Guess the smaller number!")
    elif computer>player:
        print("Gues the largger!")
    
    player= int(input("Guess the number"))

print("YOu won the number was",computer)
    

