# Mind Reading Game

import random
import time
import os

emojis =[
    "😀", "🐶","🐔","🍎","🍕","🍪", "🍓","⚽","🏓","🏹""🚗","✈️","🎻","❤️","🔥""🎉"]

def generate_table():
    magic_emoji = random.choice(emojis)
    non_magic_emojis = [emoji for emoji in emojis if emoji != magic_emoji]
    emoji_table = {}
    for num in range(1, 100):
        if num % 9 == 0:
            emoji_table[num] = magic_emoji
        else:
            emoji_table[num] = random.choice(non_magic_emojis)
    return emoji_table, magic_emoji


def display_instructions():
    print("Welcome to the MIND READING GAME!")
    time.sleep(1)
    print("\nFollow these steps carefully:\n")

    print("1. Think of any two-digit number (like 42).")
    print("2. Add both digits together (e.g, 4 + 2 = 6).")
    print("3. Subtract the sum from your original number (e.g, 42 - 6 = 36).")
    print("4. Find your number in the table below and remeber the emoji next to it.\n")


def display_table(emoji_table):
    for i in range(1, 100):
        print(f"{i:2}: {emoji_table[i]}", end="     ")
        if i % 5 == 0:
            print()
    print()


def reveal_magic_emoji(magic_emoji):
    input("\nOnce you've rememberd the symbol, press Enter and I will read your mind...")
    print("Concentrating...")
    time.sleep(2)
    print(f"The emoji you're thinking of is: {magic_emoji}\n")


def get_choice(prompt):
    choice = input(prompt).strip().lower()
    if choice in ["yes", "y"]:
        return True
    elif choice in ["no", "n"]:
        return False
    else:
        print("Invalid choice input.")


def play_game():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        emoji_table, magic_emoji = generate_table()
        display_instructions()
        display_table(emoji_table)
        reveal_magic_emoji(magic_emoji)
        if not get_choice("Do you want to play again? (Y/N): "):
            os.system("cls" if os.name == "nt" else "clear")
            break

play_game()


