WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHICS": 7}

def main():
    print(f"----- WELCOME TO THE SPELLING BEE GAME -----")
    print()
    rules = input("Do you want to go thrugh RULES? (y/n): ").lower()
    if rules in ["y", "yes"]:
        print()
        print("RULES: Guess the words from given letters. There are total four words. One of which is a SUPER-WORD which means that if you guessed that word you'll win the game all at once. If you fail to guess the word more than 3 times, the game will be over and you'll lose!")
    print()
    print("Your letters are: A I P C R H G")
    wrong_guess = 0

    while len(WORDS) > 0:
        print(f"{len(WORDS)} words left!")
        print()
        guess = input("Guess a word: ").upper()
        if guess == "GRAPHICS":
            WORDS.clear()
            print()
            print("This was a SUPER-WORD.")
            print("----- Congratulations! You've won the Game 🎉 -----")
            break
        if guess in WORDS.keys():
            points = WORDS.pop(guess)
            print()
            print(f"Good job you've got {points} points")
        else:
            print()
            print("!!!!! Wrong Guess ⚠ !!!!!")
            wrong_guess += 1
        if wrong_guess > 3:
            print("----- Game Over! -----")
            break
    print()
    show_words = input("Do you want to see what the words were? (y/n): ")
    print()
    if show_words in ["y", "yes"]:
        for word, point in WORDS.items():
            print(f"{word} was worth {point} points")


main()
