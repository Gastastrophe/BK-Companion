import tkinter as tk
import os
import random
from functools import partial
from character import character
from magnus import deck

# Shuffle a spent deck
def get_new_deck(hand, battle_deck, card_frames, message_frame):
    # Get a new deck
    battle_deck.cards = deck().cards
    random.shuffle(battle_deck.cards)
    # Draw cards equal to hand size
    hand = []
    for _ in range(player.hand_size):
        draw_card(hand, battle_deck, card_frames, message_frame)
    # Update hand frame
    update_hand(hand, battle_deck, card_frames, message_frame)

# Displays a card in the center
def display_card(played_card, message_frame):
    text = ""
    # Display spirit numbers
    text += "Spirit: "
    for num in played_card["numbers"]:
        text += str(num)
    text += "\n"
    # Display card name
    text += "Name: " + played_card["name"] + "\n"
    # Display element
    text += "Element: " +  played_card["element"] + "\n"
    # Display card combo number
    text += "Combo: " + str(played_card["combo"]) + "\n"
    # Display ATK if the Magnus has it
    if not played_card["ATK"] is None:
        text += "ATK: " +  str(played_card["ATK"]) + "\n"
    # Display DEF if the Magnus has it
    if not played_card["DEF"] is None:
        text += "DEF: " +  str(played_card["DEF"]) + "\n"
    # Display condition if the Magnus has it
    if not played_card["condition"] is None:
        text += "Condition: " +  played_card["condition"] + "\n"
    # Display card effect
    text += "Effect: " + played_card["effect"] + "\n"
    # Put the text from the played card into the display field
    message_frame.nametowidget("cardDetails").config(text = text)

# Plays a card from your hand
def play_card(i, hand, battle_deck, card_frames, message_frame):
    # Add 1 to the combo counter
    combo_counter = message_frame.nametowidget("comboCounter")
    combo_counter.config(text = combo_counter.cget("text")[:-1] + str(int(combo_counter.cget("text")[-1]) + 1))
    # Remove the played card from the hand and display it
    display_card(hand.pop(i), message_frame)
    # Draw a new card
    draw_card(hand, battle_deck, card_frames, message_frame)

# Add cards from hand to card frames
def update_hand(hand, battle_deck, card_frames, message_frame):
    # Remove all existing card widgets and create new ones for the updated hand
    for i in range(len(card_frames)):
        for widget in card_frames[i].winfo_children():
            widget.destroy()
    for i, card in enumerate(hand):
        # Make a name label, a display button and a play button
        card_name  = tk.Label(master=card_frames[i], text=card["name"], name="cardName" + str(i))
        card_name.pack()
        play_button = tk.Button(master = card_frames[i], text="Play", command = partial(play_card, i, hand, battle_deck, card_frames, message_frame))
        play_button.pack()
        display_button = tk.Button(master = card_frames[i], text="Show", command = partial(display_card, card, message_frame))
        display_button.pack()

# Draws a card from a deck
def draw_card(hand, battle_deck, card_frames, message_frame):
    # If the deck is empty, tell the user to reshuffle
    if len(battle_deck.cards) == 0:
        deck_size = message_frame.nametowidget("deckSize")
        deck_size.config(text = deck_size.cget("text")[:6] + "Please shuffle the deck")
        # Update hand visuals
        update_hand(hand, battle_deck, card_frames, message_frame)
    # Otherwise, draw a card
    else:
        # Draw a card
        hand.append(battle_deck.cards.pop(0))
        # Update deck size
        deck_size = message_frame.nametowidget("deckSize")
        deck_size.config(text = deck_size.cget("text")[:6] + str(len(battle_deck.cards)))
        # Update hand visuals
        update_hand(hand, battle_deck, card_frames, message_frame)

# Reset the combo counter and display the damage report
def end_turn(message_frame):
    combo_counter = message_frame.nametowidget("comboCounter")
    combo_counter.config(text = combo_counter.cget("text")[:-1] + str(0))

# Creates a GUI for battle
def start_battle(player):
    # Create a graphic interface
    window = tk.Tk()
    # Create an upper slot for other mesages
    message_frame = tk.Frame(master=window, width=100*8, height=300, relief=tk.SUNKEN)
    message_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
    # Create a combo counter
    combo_counter = tk.Label(master=message_frame, text="Combo: 0", name="comboCounter")
    combo_counter.place(rely=0, relx=1.0, x=0, y=0, anchor="ne")
    # Create an end turn button
    turn_ender = tk.Button(master=message_frame, text="End Turn", name="endTurn", command = lambda: end_turn(message_frame))
    turn_ender.place(rely=0, relx=0, x=0, y=0, anchor="nw")
    # Create an area to display card effects
    card_details = tk.Label(master=message_frame, text = "", name = "cardDetails")
    card_details.place(relx=0.5, rely=0.5, anchor="center")
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
    # Create a deck size label
    combo_counter = tk.Label(master=message_frame, text="Deck: " + str(len(battle_deck.cards)), name="deckSize")
    combo_counter.place(rely=1.0, relx=1.0, x=0, y=0, anchor="se")
    # Create a shuffle deck button
    deck_resetter = tk.Button(master=message_frame, text="Shuffle Deck", name="shuffleDeck", command = lambda: get_new_deck(hand, battle_deck, card_frames, message_frame))
    deck_resetter.place(rely=1.0, relx=0, x=0, y=0, anchor="sw")
    # Draw cards equal to hand size
    hand = []
    for _ in range(player.hand_size):
        draw_card(hand, battle_deck, card_frames, message_frame)

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