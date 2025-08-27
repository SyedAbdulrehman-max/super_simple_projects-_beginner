def item_view():
    if user_choice == 1:
        print("View mode:")
        with open("list.txt","r") as f:
            print("\n",f.read())
            
def item_add():
    if user_choice == 2:
        print("Add mode:")
        modify = input("Enter to add item in list...!")
        with open("list.txt","r") as f:
            item = f.read()
        with open("list.txt","a") as f:
            add = f.write(modify + "\n")
            print(f"{modify} is add in list:")

def item_deletion():
    if user_choice == 3:
        print("Deletion mode: ")
        item_del = input("Enter item to delet: ")

        with open("list.txt","r")as f:
            dele = f.read().splitlines()

            if item_del in dele:
                dele.remove(item_del)

                with open("list.txt","w") as f:
                    for item in dele:
                        f.write(item+"\n")
                print(f"'{item_del}' has been deleted!")

            else:
                print("item not found::")
        
while True:
    print("1. View list\n2. Add item\n3. Delete item\n4. Exit")
    user_choice = int(input("Enter you choice(1,2,3,4):"))

    if user_choice == 1:
        item_view()
    elif user_choice == 2:
        item_add()
    elif user_choice == 3:
        item_deletion()
    elif user_choice == 4:
        print("File has been updated....!")
        break