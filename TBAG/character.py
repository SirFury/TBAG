class Character():
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self):
        print(f"{self.name} is in this room")
        print(self.description)

    def set_conversation(self, conversation):
        self.conversation = conversation

    def talk(self):
        if self.conversation is not None:
            print(f"[{self.name}] says: {self.conversation}")
        else:
            print(f"{self.name} ignores you.")

    def interact(self, combat_item, gift_item, bribe_item):
        print(f"{self.name} doesn't want to fight with you.")
        return True
       
    def describe(self):
        print(self.name + " is here!")
        print(self.description)

class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.weakness
    
    def interact(self, combat_item):
        if combat_item == self.weakness: # You can add .lower() to ensure capitalisation doesn't matter
            print(f"You fend off {self.name} with the {combat_item}.")
            return True
        else:
            print(f"{self.name} uses a bone to smash your head, ending you instantly!")
            return False
        
class Frenemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.weakness
    
    def interact(self, bribe_item):
        if bribe_item == self.weakness:
            print(f"You bribe {self.name} with the {bribe_item} and he lets you pass.")
            return True
        else:
            print(f"{self.name} sucks you dry, ending you instantly!")
            return False
        

class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.weakness
    
    def interact(self, gift_item):
        if gift_item == self.weakness:
            print(f"You gift {self.name} with the {gift_item} and in return, he gives you some cheese and blood.")
            return True
        else:
            print(f"{self.name} kicks you out of the game!")
            return False
            
    