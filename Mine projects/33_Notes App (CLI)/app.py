#   Wellcome

wellcome="Wellcome to Notes"
print(wellcome)
print("="*len(wellcome))

#inputs

while True:
    print('1.ADD\n2.READ\n3.DELETE\n4.EXIT')
    menu = int(input(">"))

    if  menu not in [1,2,3,4]:
        print("INVILD OPTION :>")
    elif menu == 1:
        print("Enter your text: ")
        add = input(">")
        with open('notes.txt','a',encoding="utf-8") as f:
            f.write('\n' + add)
        print('1.Menu\n2.EXIT')
        check = input('>').lower()
        if check  == "1" or check == 'again':
            continue
        elif check == '2' or check == 'exit':
            break 
    elif menu == 2:
        with open('notes.txt') as f:
           read = f.read()
        print("="*15)
        print(read)
        print("="*15)
        print('1.Menu\n2.EXIT')
        check = input('>').lower()
        if check  == "1" or check == 'again':
            continue
        elif check == '2' or check == 'exit':
            break 
    elif menu == 3:
        print("Enter the text you want to delete:")
        delete = input(">")

        # Step 1: Read all lines
        with open("notes.txt", "r", encoding="utf-8") as f:
                lines = f.readlines()

    # Step 2: Remove lines that match
        new_lines = [line for line in lines if line.strip() != delete.strip()]

        if len(new_lines) != len(lines):  # means something was deleted
            with open("notes.txt", "w", encoding="utf-8") as f:
                f.writelines(new_lines)
            print("Deleted successfully!")
        else:
            print("Finding...")
            print("NOT FOUND..")

        # Menu again
        print("1.Menu\n2.EXIT")
        check = input(">").lower()
        if check == "1" or check == "again":
            continue
        elif check == "2" or check == "exit":
            break
    elif menu == 4:
        print("Thanks for choceing us")
        break
