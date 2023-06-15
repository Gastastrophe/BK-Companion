import glob
import json

"""
ALL Magnus have:
- a list of numbers used for creating hands
- a name
- an element
- a class that can use it, or "General"
- a minimum number of cards needed to be played before it "combo" - 1
- a description of the effect of the card

SOME Magnus have:
- an ATK value for damage (+) or healing (-)
- a DEF value for blocking
- a condition to apply to the target
"""
class magnus(dict):
    def __init__(self, numbers, name="default name", element="Physical", char_class="General", ATK=None, DEF=None, condition=None, combo=1, effect="default description"):
            dict.__init__(self, numbers=numbers, name=name, element=element, char_class=char_class, ATK=ATK, DEF=DEF, combo=combo, condition=condition, effect=effect)

class deck():
    def __init__(self):
        self.cards = []
        for file in glob.glob("deck/*.json"):
            with open(file, 'r') as openfile:
                # Reading the character from a json file
                magnus_json = json.load(openfile)
            self.cards.append(magnus(numbers=magnus_json["numbers"], name=magnus_json["name"], element=magnus_json["element"], char_class=magnus_json["char_class"], ATK=magnus_json["ATK"], DEF=magnus_json["DEF"], condition=magnus_json["condition"], combo=magnus_json["combo"], effect=magnus_json["effect"]))