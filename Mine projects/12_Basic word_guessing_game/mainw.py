lives = 5
word = ['a', 'b', 'c']
display = ['_'] * len(word)  # current state of guesses

while True:
    guess = input("Guess a letter: ")

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
        print("Correct:", ' '.join(display))
    else:
        lives -= 1
        print(f"Wrong! Lives left: {lives}")

    if '_' not in display:
        print("You won!")
        break
    elif lives == 0:
        print("You lost!")
        break

    continue