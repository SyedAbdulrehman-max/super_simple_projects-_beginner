import random
char  = "abcdefghijklmnopqrstuvwxyz!@#$%^&()_-=+-"
length  = int(input("Enter the length of password: "))
password = ""
for i in range(length):
    password+=random.choice(char)

print(f"Your password is {password}")