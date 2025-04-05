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
    def __init__(self, numbers, name="default name", element="Physical", char_class="General", PHYS_ATK=0, PHYS_DEF=0, FIRE_ATK=0, FIRE_DEF=0, WATER_ATK=0, WATER_DEF=0, LIGHT_ATK=0, LIGHT_DEF=0, DARK_ATK=0, DARK_DEF=0, WIND_ATK=0, WIND_DEF=0, TIME_ATK=0, TIME_DEF=0, condition=None, combo=1, effect="default description"):
            dict.__init__(self, 
                          numbers=numbers, 
                          name=name, 
                          element=element, 
                          char_class=char_class, 
                          PHYS_ATK=PHYS_ATK, 
                          PHYS_DEF=PHYS_DEF, 
                          FIRE_ATK=FIRE_ATK, 
                          FIRE_DEF=FIRE_DEF, 
                          WATER_ATK=WATER_ATK, 
                          WATER_DEF=WATER_DEF, 
                          LIGHT_ATK=LIGHT_ATK, 
                          LIGHT_DEF=LIGHT_DEF, 
                          DARK_ATK=DARK_ATK, 
                          DARK_DEF=DARK_DEF, 
                          WIND_ATK=WIND_ATK, 
                          WIND_DEF=WIND_DEF, 
                          TIME_ATK=TIME_ATK, 
                          TIME_DEF=TIME_DEF, 
                          combo=combo, 
                          condition=condition, 
                          effect=effect)

class deck():
    def __init__(self):
        self.cards = []
        for file in glob.glob("deck/*.json"):
            with open(file, 'r') as openfile:
                # Reading the character from a json file
                magnus_json = json.load(openfile)
                self.cards.append(magnus(numbers=magnus_json["numbers"], 
                                        name=magnus_json["name"], 
                                        element=magnus_json["element"], 
                                        char_class=magnus_json["char_class"], 
                                        PHYS_ATK=magnus_json["PHYS_ATK"], 
                                        PHYS_DEF=magnus_json["PHYS_DEF"], 
                                        FIRE_ATK=magnus_json["FIRE_ATK"], 
                                        FIRE_DEF=magnus_json["FIRE_DEF"], 
                                        WATER_ATK=magnus_json["WATER_ATK"], 
                                        WATER_DEF=magnus_json["WATER_DEF"], 
                                        LIGHT_ATK=magnus_json["LIGHT_ATK"], 
                                        LIGHT_DEF=magnus_json["LIGHT_DEF"], 
                                        DARK_ATK=magnus_json["DARK_ATK"], 
                                        DARK_DEF=magnus_json["DARK_DEF"], 
                                        WIND_ATK=magnus_json["WIND_ATK"], 
                                        WIND_DEF=magnus_json["WIND_DEF"], 
                                        TIME_ATK=magnus_json["TIME_ATK"], 
                                        TIME_DEF=magnus_json["TIME_DEF"], 
                                        condition=magnus_json["condition"], 
                                        combo=magnus_json["combo"], 
                                        effect=magnus_json["effect"]))