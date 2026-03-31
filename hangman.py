import random

words = ["python", "java", "hangman", "computer", "science", "television", "mobile", "refrigirator", "light", "god", "father", "mother"]

def play_game():
    word = random.choice(words).lower()
    guessed_letters = []
    attempts = 6

    print("\nWelcome to Hangman Game!")

    while attempts > 0:
        display_word = ""

        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord:", display_word.strip())

        if "_" not in display_word:
            print("You guessed the word! Congratulations!")
            return "win"

        guess = input("Enter a letter or guess the whole word: ").lower()

        if guess == word:
            print("Perfect! You guessed the whole word correctly!")
            return "win"

        if len(guess) > 1:
            print("Wrong word guess!")
            attempts -= 1
            print("Attempts left:", attempts)
            continue

        if guess in guessed_letters:
            print("Already guessed!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct letter!")
        else:
            attempts -= 1
            print("Wrong letter! Attempts left:", attempts)

    print("Game Over! The word was:", word)
    return "lose"


while True:
    result = play_game()

    if result == "win":
        choice = input("Excellent! Ready for another challenge? (y/n): ").lower()
    else:
        choice = input("Game over! Want to give it another try? (y/n): ").lower()

    if choice != 'y':
        print("Thanks for playing Hangman! See you again.")
        break