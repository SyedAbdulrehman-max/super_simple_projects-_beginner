print("Welcome to Mad Libs! Fill in the blanks to create a funny story.\n")

name = input("Enter a name: ")
place = input("Enter a place: ")
adjective = input("Enter an adjective: ")
object_word = input("Enter an object: ")
animal = input("Enter an animal: ")
verb = input("Enter a verb: ")
name_two = input("Enter another name: ")
adjective2 = input("Enter another adjective: ")
number = input("Enter a number: ")
food = input("Enter a food (plural): ")

print(f'''
One day, {name} decided to visit the {place}.
It was a very {adjective} day, so they carried a {object_word}.
On the way, they saw a {animal} that could {verb}.
Surprised, {name_two} shouted, "Wow, that’s {adjective2}!"
Finally, they went home and ate {number} {food}.
''')
 