import random
import hangmanwordbank

print("888")
print("888")
print("888")
print("88888b.  8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b.")
print("888 888b    888b888 888bd88P888b888 8888 888b    888b888 888b")
print("888  888.d888888888  888888  888888  888  888.d888888888  888")
print("888  888888  888888  888Y88b 888888  888  888888  888888  888")
print("888  8888Y888888888  888 8Y88888888  888  8888Y888888888  888")
print("                             888")
print("                        Y8b d88P                              ")
print("                         8Y88P8                               ")

chosen_word = random.choice(hangmanwordbank.words)

lives = 7

display = []

for letter in chosen_word:
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(hangmanwordbank.HANGMANPICS[7 - lives])
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win.")
