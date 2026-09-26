# Word Guessing Game
# Try to discover the secret word using the hints provided.
# Each hint shows which letters are correct and which ones need to move.

print("Welcome to the Word Guessing Game!")

secret_word = "student"
guess_count = 0

# Display the initial hint
initial_hint = "_ " * len(secret_word)
print("Your hint is:", initial_hint)

while True:

    guess = input("What is your guess? ").lower()

    # Count every guess the user makes
    guess_count += 1

    # Check if the guess is correct
    if guess == secret_word:
        print("You got it right!!")
        print("Number of guesses:", guess_count)
        break

    # Check if the guess has the correct length
    elif len(guess) == len(secret_word):

        hint = ""

        # Check each letter
        for i in range(len(guess)):

            # Correct letter in the correct position
            if guess[i] == secret_word[i]:
                hint += guess[i].upper()

            # Correct letter in the wrong position
            elif guess[i] in secret_word:
                hint += guess[i].lower()

            # Letter is not in the secret word
            else:
                hint += "_"

        print("Your hint is:", " ".join(hint))

    # Guess has the wrong number of letters
    else:
        print("Sorry, your guess must have the same number of letters")
        print("as the secret word.")
