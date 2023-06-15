import json

# Contains modifiers and descriptions for character background elements
class background(dict):
    def __init__(self, name="default", description="default", positive="default", negative="default"):
        dict.__init__(self, name = name, description = description, positive = positive, negative = negative)

# Defines a character
class character():
    # Assign level 1 stats on creation. if mode=1, then skip adding classes, adding backgrounds, and saving the character
    def __init__(self, mode=0, name="character"):
        self.name = name
        self.level = 1
        self.backgrounds = []
        if mode == 0:
            print("Choose your character class by inputting a number:")
            print("1. Knight")
            print("2. Shepherd")
            print("3. Mage")
            print("4. Crafter")
            choice = input()
            if choice == "1":
                self.char_class = "Knight"
            elif choice == "2":
                self.char_class = "Shepherd"
            elif choice == "3":
                self.char_class = "Mage"
            elif choice == "4":
                self.char_class = "Crafter"
            else:
                print("Invalid choice. Using default class")
                self.char_class = "Knight"
            print("Describe your character's physicality:\n")
            self.add_background()
            print("Describe your character's demeanor:\n")
            self.add_background()
            print("Describe your character's homeland:\n")
            self.add_background()
            print("Describe your character's current occupation:\n")
            self.add_background()
        self.set_hand()
        self.set_combo_max()
        if mode == 0:
            self.save(name)
    
    # Set hand size and combo max based on current level
    def set_hand(self):
        self.hand_size = 2 + self.level
    def set_combo_max(self):
        self.combo_max = 1 + self.level

    # Gets user input for background traits and returns a background object
    def add_background(self):
        name = input("\nEnter the name of your background\n")
        description = input("Enter a description of your background\n")
        positive = input("Describe when this background would increase your odds of success\n")
        negative = input('Describe when this background would decrease your odds of success\n')
        self.backgrounds.append(background(name, description, positive, negative))

    # Save the character as a json
    def save(self, name="character"):
        # Serializing the caharacter sheets as a json string
        json_object = json.dumps(self.__dict__)
 
        # Write the json string to a file
        with open("characters/" + name + ".json", "w") as outfile:
            outfile.write(json_object)

    # load a character from a file
    def load(self, name="character"):
        with open("characters/" + name + '.json', 'r') as openfile:
            # Reading the character from a json file
            char_json = json.load(openfile)
        self.name = char_json["name"]
        self.level = char_json["level"]
        self.char_class = char_json["char_class"]
        self.backgrounds = []
        for bgd in char_json["backgrounds"]:
            self.backgrounds.append(background(bgd["name"], bgd["description"], bgd["positive"], bgd["negative"]))
        self.set_hand()
        self.set_combo_max()