quiz = [
    {
        "question": "What is the capital of Pakistan?",
        "options": ["Lahore", "Islamabad", "Karachi", "Multan"],
        "answer": "Islamabad"
    },
    {
        "question": "Which data type is used to store multiple values in Python?",
        "options": ["int", "str", "list", "bool"],
        "answer": "list"
    },
    {
        "question": "What does 'if' statement do in Python?",
        "options": ["Repeats code", "Stores data", "Makes decisions", "Defines a function"],
        "answer": "Makes decisions"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "<!-- -->", "#", "%"],
        "answer": "#"
    },
    {
        "question": "What will len('apple') return?",
        "options": ["4", "5", "6", "error"],
        "answer": "5"
    }
]

for i in quiz:

    print(i["question"])

    print(i['options'])

    user_choice= str(input("Enter answer:"))
    
    if user_choice == i["answer"]:
        print("Correct!")
    else:
        print("Wrong!")