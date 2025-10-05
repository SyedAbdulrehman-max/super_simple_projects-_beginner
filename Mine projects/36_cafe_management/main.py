menu = {
    'pizza': 40,
    'pasta': 50,
    'burger': 60,
    'salad': 70,
    'coffee': 80,
}

print("Welcome to our restaurant. Here's the menu:")
for food, price in menu.items():
    print(f"{food.title()}: Rs{price}")

total = 0

while True:
    item = input("Enter your item (or type 'done' to finish): ").lower()
    
    if item == "done":
        break
    elif item in menu:
        total += menu[item]
        print(f"Added {item}. Current total: Rs{total}")
    else:
        print(f"Sorry, {item} is not available.")

print(f"Your final total is Rs{total}")
