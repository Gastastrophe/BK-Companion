import tkinter as tk
import os
import random
from functools import partial
from character import character
from magnus import deck

# Shuffle a spent deck
def get_new_deck(hand, battle_deck, card_frames):
    # Get a new deck
    battle_deck.cards = deck().cards
    # Draw cards equal to hand size
    hand = []
    for _ in range(player.hand_size):
        draw_card(hand, battle_deck, card_frames)

# Plays a card from your hand
def play_card(i, hand, battle_deck, card_frames):
    hand.pop(i)
    draw_card(hand, battle_deck, card_frames)

# Add cards from hand to card frames
def update_hand(hand, battle_deck, card_frames):
    for i, card in enumerate(hand):
        for widget in card_frames[i].winfo_children():
            widget.destroy()
        label = tk.Button(master = card_frames[i], text=card["name"], command = partial(play_card, i, hand, battle_deck, card_frames))
        # Pack the button into the hand region
        label.pack()

# Draws a card from a deck
def draw_card(hand, battle_deck, card_frames):
    hand.append(battle_deck.cards.pop(0))
    update_hand(hand, battle_deck, card_frames)



# Creates a GUI for battle
def start_battle(player):
    # Create a graphic interface
    window = tk.Tk()
    # Create an upper slot for other mesages
    message_frame = tk.Frame(master=window, width=100*8, height=300, relief=tk.SUNKEN)
    message_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
    # Assign the lower half for cards
    card_zone = tk.Frame(master=window, width=100*8, height=100)
    card_zone.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
    # Create 8 slots for 8 cards
    card_frames = []
    for _ in range(8):
        frame = tk.Frame(master=card_zone, width=100, height=100, relief=tk.RIDGE)
        frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        card_frames.append(frame)
    # Set up a deck
    battle_deck = deck()
    random.shuffle(battle_deck.cards)
    # Draw cards equal to hand size
    hand = []
    for _ in range(player.hand_size):
        draw_card(hand, battle_deck, card_frames)

    # Update the window to update it
    window.mainloop()


###### Load the character ######

player_name = input("Please enter your character name\n")

if os.path.exists("characters/" + player_name + ".json"):
    print('Loading character ' + player_name + "...")
    player = character(1)
    player.load(player_name)
else:
    choice = input("No character named " + player_name + " found. Create a new character? y/n: ")
    if choice.lower() == "y":
        player = character(0, name=player_name)
    else:
        exit()

###### Open combat window ######

start_battle(player=player)