import random
import hangman_stages

word_list = ["apple", "snowfall", "kashmir"]
lives = 6
chosen_word = random.choice(word_list)

print("Welcome to Hangman!")

# Display underscores for each letter
display = ["_"] * len(chosen_word)
print("Current word:", " ".join(display))

game_over = False

while not game_over:
    guessed_letter = input("Guess a letter: ").lower()

    if guessed_letter in chosen_word:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guessed_letter:
                display[position] = guessed_letter
        print("Good guess!")
    else:
        lives -= 1
        print(f"Wrong guess! Lives left: {lives}")
        if lives == 0:
            game_over = True
            print("BAD LUCK! You lose !!")

    print("Current word:", " ".join(display))
    print(hangman_stages.stages[6 - lives])  #

    if "_" not in display:
        game_over = True
        print("CONGRATULATIONS! You win the game! Hope you enjoyed it!!")
