
while True:
    word = input("Check word/number is Palindrome: ").lower()
    word = word.replace(" ","")
    r = word[::-1]
    
    if word == r :
        print(f'The word {word} is Palindrome ')
        
    else:
        print(f'The word {word} is not palindrome')
        

    choice = int(input('1.Check again\n2.Exit (1/2) '))
    
    if choice not in  [1,2]:
        print('invild choice')
        continue
    
    elif choice == 1:
        print('Check again!')
        continue
    
    else:
        print("see you later!")
        break