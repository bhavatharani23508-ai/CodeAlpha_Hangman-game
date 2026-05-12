import random
secret_words = [
    "laptop",
    "network",
    "science",
    "python",
    "developer"
]
chosen_word = random.choice(secret_words)
lives = 6
used_letters = []
hidden_word = []
for ch in chosen_word:
    hidden_word.append("_")
print("\n====== HANGMAN GAME ======\n")
print("Guess the hidden word letter by letter.")
print("You only have 6 wrong attempts.\n")
while lives > 0:
    print("Word :", " ".join(hidden_word))
    print("Wrong Attempts Left :", lives)
    print("Used Letters :", ", ".join(used_letters))
    user_letter = input("\nEnter a letter : ").lower()
    if len(user_letter) != 1:
        print("Enter only ONE letter.\n")
        continue
    if not user_letter.isalpha():
        print("Only alphabets are allowed.\n")
        continue
    if user_letter in used_letters:
        print("You already tried this letter.\n")
        continue
    used_letters.append(user_letter)
    if user_letter in chosen_word:
        print("Good Guess!\n")
        index = 0
        for letter in chosen_word:
            if letter == user_letter:
                hidden_word[index] = user_letter
            index += 1
    else:
        lives -= 1
        print("Wrong Letter!\n")
    if "_" not in hidden_word:
        print(" Congratulations!")
        print("You guessed the word :", chosen_word)
        break
if "_" in hidden_word:
    print("\n You Lost the Game")
    print("Correct Word was :", chosen_word)
