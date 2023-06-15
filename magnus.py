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
            self.cards.append(magnus(magnus_json["numbers"], magnus_json["element"], magnus_json["char_class"], magnus_json["ATK"], magnus_json["DEF"], magnus_json["condition"], magnus_json["combo"], magnus_json["effect"]))