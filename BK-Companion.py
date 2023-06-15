import tkinter as tk
import os

from character import character
from magnus import deck, magnus

# Create a graphic interface
window = tk.Tk()

# Call this to update it
window.update()


###### Load the character ######

player_name = input("Please enter your character name\n")

if os.path.exists("characters/" + player_name + ".json"):
    print('Loading character ' + player_name + "...")
    player = character(1).load(player_name)
else:
    choice = input("No character named " + player_name + " found. Create a new character? y/n: ")
    if choice.lower() == "y":
        player = character(0, name=player_name)
    else:
        exit()

###### Load the cards in the deck ######

cards = deck()
print(cards.cards)