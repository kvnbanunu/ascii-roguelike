import os
import sys

run = True
menu = True
play = False
rules = False

HP = 50
ATK = 3

# clears the terminal
def clear():
    if sys.platform.startswith("linux") or sys.platform.startswith("darwin"):
        os.system("clear")
    else:
        os.system("cls")

def draw():
    print("--------------------")

def save():
    lst = [
        name,
        str(HP),
        str(ATK)
    ]

    with open("load.txt", "w") as f:
        for item in lst:
            f.write(f"{item}\n")

def load():
    lst = []
    with open("load.txt", "r") as f:
        for line in f:
            lst.append(line[0:-1]) #deleting "\n"
    return lst

while run:
    while menu:
        clear()
        draw()
        print("1. NEW GAME")
        print("2. LOAD GAME")
        print("3. RULES")
        print("4. QUIT GAME")
        draw()

        if rules:
            print("These are the rules:")
            rules = False
            choice = ""
            input("> ")
        else:
            choice = input("# ")

        if choice == "1":
            clear()
            name = input("# What is your name? ")
            menu = False
            play = True
        elif choice == "2":
            name, HP, ATK = load() #unpacking saved lst
            clear()
            print(f"Welcome back {name}!")
            input("> ")
            menu = False
            play = True
        elif choice == "3":
            rules = True
        elif choice == "4":
            clear()
            quit()

    while play:
        save() #autosave

        clear()
        draw()
        print("0 - SAVE AND QUIT")
        draw()

        dest = input("# ")

        if dest == "0":
            play = False
            menu = True
            save()
