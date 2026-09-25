
print("Welcome to the word guessing game!")
secret_word = "student"
while True:
    print("Your hint is _ _ _ _ _ _ _")
    guess = input("Enter a word: ")
    if len(guess) != len(secret_word):
        print("Sorry, the guess must have the same number of letters as the secret word.")
        for i, ch in enumerate(guess):
            if ch == secret_word[i]:
                guess[i].upper()
                print(f"Your hint is: {ch}")

            i2 = secret_word.find(ch)
            if ch in secret_word and i == i2 :
                guess[i].lower
                print(f"your hint is: {ch}")