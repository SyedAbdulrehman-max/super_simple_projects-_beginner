import random

subjects = [
    "Hamza",
    "Ali",
    "Fawad Khan",
    'A Lahore dog',
    'A group of monkey',
    'Prime Ministry of Pakistan'    
]

actions = [
    "lunches",
    "cancal",
    "dances",
    "eats",
    "declare war on",
    "orders", 

]
places = [
    "at red fort",
    "train on tracke",
    "plate of samosa",
    "Parliment of pakistan",
    "Pakistan enternce",
    "GeO",
]

while True:
    
    print('For News Enter: 1  \nTo Exit Enter: 2')
    choice = int(input('>'))
    if choice != 1  and choice != 2:
        print('Invilad Choice!')
    elif choice == 1:
        print(f'{random.choice(places)}')
    else:
        break
print('Thanks for using our service!')