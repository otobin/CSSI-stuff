import random
random_word_list = ["programming", "cssi", "computers", "projector"]
word = random_word_list[random.randint(0, len(random_word_list)-1)]
print(word)
guesses = "Guesses: "
display = list("-" * len(word))
for letter in display:
    print(letter),
numGuesses = 0
maxGuesses = 5
gameOver = False
match = False
while(gameOver == False):
    match = False
    guess = raw_input("\nGuess a letter in the mystery word: ")
    for i in range(0, len(word)):
        if (guess == word[i]):
            display[i] = guess
            match = True
    if (match == False):
        guesses += guess
        guesses += " "
        numGuesses += 1
    for letter in display:
        print(letter),
    print("\n" + guesses)
    if (numGuesses > maxGuesses) or ("-" not in display):
        gameOver = True
    else:
        gameOver = False
