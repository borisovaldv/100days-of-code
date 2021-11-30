import random
from stages import logo, art
from words import words_hangman

print(logo)
chosen_word = random.choice(words_hangman)
lives = 6

display = list(len(chosen_word) * '_')
guessed = []
while '_' in display:

    if lives == 0:
        print('You lose.')
        print(f'The word was: {chosen_word}')
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed and guess in display:
        print(f'You have already guessed {guess}')

    elif guess in chosen_word:
        for i in range(len(chosen_word)):
            letter = chosen_word[i]
            if letter == guess:
                display[i] = letter

    elif guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1

    guessed += guess
    print(*display)
    print(art[lives])

if '_' not in display:
    print(*display)
    print(art[lives])
    print('You win.')