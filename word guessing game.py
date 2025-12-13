#Guess the rapper's names!

import random
word_bank = ['krsna', 'nas', 'kendrick', 'eminem', 'tupac']
word = random.choice(word_bank)
guessedword = ['_'] * len(word)
attempt = 10

while attempt > 0:
    print('\nCurrent word: ' + ' '.join(guessedword))

    guess = input("Guess a letter:").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedword[i] = guess
        print("Great guess!")
    else:
        attempt -= 1
        print("Wrong guess! Attempts left: " + str(attempt))

    if '_' not in guessedword:
        print("\nCongratulations! You have guessed the word: " + word)
        break

if attempt == 0 and '_' in guessedword:
    print("\nYou\'ve run out of attempts! The word was: " + word)
