# To convert user input into ascii art

from pyfiglet import Figlet
import random

figlet = Figlet()
fonts = figlet.getFonts()

def main():
    select_font = None

    if choose_font():
        selected_fonts = random.sample(fonts, 30)
        for font in selected_fonts:
            print(font, end=", ")
        print()

        while True:
            select_font = input("Enter font: ")
            if select_font in selected_fonts:
                break
            else:
                print("Invalid font!")

    text = input("Input: ")

    figlet_art(text, select_font)



def choose_font():
    choice = input("Do you want to choose font?(y/n): ").strip().lower()
    if choice in ["y", "yes"]:
        return True
    else:
        return False


def figlet_art(text, font = None):
    if font == None:
        font = random.choice(fonts)
    figlet.setFont(font = font)
    print(figlet.renderText(text))


main()
