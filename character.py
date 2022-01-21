'''
Creating a Character class and also extending it to Enemy and Friend class
'''


class Character:

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        print("")
        print(self.name + " is here!")
        print(self.description)

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True


class Enemy(Character):

    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def get_weakness(self):
        return self.weakness

    def set_weakness(self, char_weakness):
        self.weakness = char_weakness

    # Override the 'fight()' method of the base class 'Character'
    def fight(self, combat_item):
        if self.weakness == combat_item:
            print("You fend off " + self.name + " with the " + combat_item)
            return True
        else:
            print(self.name + " crushed you, puny adventurer!")
            return False


class Friend(Character):

    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.gift = None

    def get_gift(self):
        return self.gift

    def receive_gift(self):
        print(self.name + " gifted you " + self.gift + "!!!")

    def set_gift(self, char_gift):
        self.gift = char_gift
