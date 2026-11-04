import random
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

# Create placeholder
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(f"Word to guess: {placeholder}")

game_over = False
correct_letters = []
lives = 6

while not game_over:

    print(f"****************************{lives} LEFT****************************")
    guess = input("Guess a letter: ").lower()

    # TODO-4: Already guessed check
    if guess in correct_letters:
        print(f"You've already guessed {guess}")
        continue

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    # TODO-5: Wrong guess check
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1

        if lives == 0:
            game_over = True
            # TODO-7: Correct word show
            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # TODO-2: Use stages
    print(stages[lives])