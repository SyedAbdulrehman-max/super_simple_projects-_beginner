import time

print("Wellceom to game  ")

time.sleep(1)

print('Treasure Hunt')
time.sleep(1)
print('1.Start\n2.Exit')
time.sleep(1)
start_or_stop = int(input('>'))

if start_or_stop not in [1,2]:
    print('Invild Choice!')   
elif start_or_stop == 2:
    print('Thanks for playing !')
    time.sleep(1)
    print('See you later!')

else: 
    print('Game is started!')

    print('You wake up in a small stone room. There,s a door in the front of you and a wooden box on the floor.')
    print('Want to open the wooder box!')
    
    while True:

        #opening the first room door/starting room

        #found the box

        woodenbox = (input('yes/no > ')).lower()

        if woodenbox == 'yes' or woodenbox == 'y':
            print('opening....')
            time.sleep(2)
            print('Opened !')
            time.sleep(1)
            print('YOu find the door key !') 
            time.sleep(1)
            print('Now you can open the Door')
            break
        

        elif woodenbox == 'no' or woodenbox == 'n':
            print('You looking around the empty room')
            time.sleep(2)
            print('Found nothing ! ')
            time.sleep(1)
            print('Open the box ?')
            continue
        else:
            print('invild choice!')
        

    #Hall way
    
    while True:

        print('open the door!')
        open_door = input("(y/n):> ")
        
        if open_door == 'y':
            print('Unlocking the door....')
            time.sleep(2)
            print('Door is unlocked!')
            time.sleep(1)
            print('You now entered the hallway')
            break
        elif open_door == 'n':
            print('what are you waiting for !')
            time.sleep(1)
            print('Open the door')
            continue
    print('You found the creepy lady on laying on bed watching tv and in front there is a door  ')
    time.sleep(1)
    print('want to look around to found the main door key')

    while True:

        findingkey =  input("(y/n) > ")

        if findingkey == 'y':
            print('You sneak to explore in halway ')
            time.sleep(1)
            print('Final`y find a key')
            time.sleep(1)
            print('side to the creepy lady')
            time.sleep(1)
            print('Pick the key or wait')
            takingkey = input('(pick/wait) >').lower()
            if takingkey == 'pick':
                print('creapy lady caout you!')
                time.sleep(2)
                print('You dead..!')
                exit()
            elif takingkey =='wait':
                print('lady is going to the kitchen.... ')
                time.sleep(1)
                print('Now this is good chance to take the key')
                print('Pick a key or wait')
                taking = input('(Take/wait) >').lower()
                if taking == 'take':
                    print('You got key')
                    time.sleep(1)
                    print('Runing towards the main door')
                    time.sleep(1)
                    print('Opening the door...')
                    time.sleep(2)
                    print('You escaped')
                    exit()
                elif taking== 'wait':
                    print('lady came back ')
                    time.sleep(1)
                    print('He saw you ')
                    time.sleep(1)
                    for i in range(1,9):
                        print("RUN!")
                    time.sleep(2)
                    print("she cought you")
                    time.sleep(1)
                    print('You dead')
                    exit()

        elif findingkey =='n':
            print('you got tried ')
            print("Look around")
            continue


