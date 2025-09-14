import random
while True:
    flashcards = [
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "Who created Python?", "answer": "Guido van Rossum"},
        {"question": "What is 2 + 2?", "answer": "4"}
    ]
    card = random.choice(flashcards)
    print(f"Question: {card['question']}")

    choice  = input("Want to see the Answar (y/n)")

    if choice == "y":
        print(f"Answar:{card['answer']}")
        break
    elif choice == "n":
        ans = input("Enter the answar:")
        if ans == card["answer"]:
            print("Answar is corrected")
            break
        elif ans != card['answer']:
            print('wronge answar')
            continue