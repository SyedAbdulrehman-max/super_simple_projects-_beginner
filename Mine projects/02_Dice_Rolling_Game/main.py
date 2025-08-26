import random
dies = int(input("Enter the number of dies: "))
user = input("Roll the dice (y/n): ").lower()
number = 1

while True:
    if user == "y":
        if dies == 1:
            print(f"({random.randint(1,13)})")
        else:
            n1 =random.randint(1,12)
            n2 =random.randint(1,12)
            print(f"({n1},{n2})")
            number+=1
        break
    elif user=="n":
        print("Thanks for playing!")
        break
    else:
        print("invlid char! ") 
    user = input("Try angian: ")

print(f"You roll the dies {number}")
