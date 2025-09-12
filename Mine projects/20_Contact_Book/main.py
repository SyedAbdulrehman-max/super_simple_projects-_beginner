import json


#load contacts 

def load_contacts():

    try:
        with open('contact.json','r') as f:
            return  json.load(f)
    except FileNotFoundError:
        print('File not found....')
    except json.JSONDecodeError:
        return {}
    
# save contact

def save_contact(contacts):
    with open('contact.json','w') as f:
        json.dump(contacts,f,indent=4)

# contact book

def contact_book():
    contacts = load_contacts()

    while True:

        print('Contect book')
        menu = int(input('1.ADD\n2.Veiw\n3.Delete\n4.Exit\n(1/2/3/4)\n'))
        if menu not in [1,2,3,4]:
            print('Invild choice')
            check = int(input('1.Menu\n2.Exit\n'))
            if check == 1 :
                continue
            if check == 2:
                break

        elif menu == 1 :
            name = input('Enter name: ')
            number = input('Enter phone number: ')
            contacts[name] = number
            save_contact(contacts)
            print(f'{name} succefuly add!')
            check = int(input("1.Menu\n2.Exit\n"))
            if check == 1 :
                continue
            if check == 2:
                break

        elif menu == 2:
            with open('contact.json') as f:
                print(json.load(f))
            check = int(input("1.Menu\n2.Exit\n"))
            if check == 1 :
                continue
            if check == 2:
                break        

        elif menu == 3 :
            delete = input("Enter name to delete: ")
            if delete in contacts:
                del contacts[delete]
                save_contact(contacts)
                print(f'{delete} is succefuly deleted')
            else:
                print(f'{delete} is not found in contact file...')
            check = int(input("1.Menu\n2.Exit\n"))
            if check == 1 :
                continue
            if check == 2:
                break 

        else:
            print('Bye!Have a good day!')
        



contact_book()