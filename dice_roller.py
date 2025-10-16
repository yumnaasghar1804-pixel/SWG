import random

def dice_roller():
    print("🎲 Welcome to Dice Roller Game!")
    while True:
        choice = input("Press Enter to roll dice or type 'exit' to quit: ")
        if choice.lower() == "exit":
            print("Thanks for playing! 💖")
            break
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"🎲 You rolled: {dice1} and {dice2} (Total: {dice1 + dice2})")

dice_roller()