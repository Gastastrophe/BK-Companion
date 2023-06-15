import tkinter as tk
from character import character
import os

# Create a graphic interface
window = tk.Tk()

# Call this to update it
window.update()

player_name = input("Please enter your character name")

if os.path.exists("characters/" + player_name + ".json"):
    print('Loading character ' + player_name + "...")
    player = character(1)
    player = player.load(player_name)
else:
    choice = input("No character named " + player_name + " found. Create a new character? y/n: ")
    if choice.lower() == "y":
        player = character(0, name=player_name)
    else:
        exit()