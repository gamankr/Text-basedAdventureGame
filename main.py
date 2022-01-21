from room import Room
from character import Character, Enemy, Friend

# Initializing objects (rooms) using Room class
kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies")
kitchen.describe()

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor; huge candlesticks guard the entrance")

dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall")

# Linking rooms
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")  # Rooms should be linked in the opposite direction also

dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

# Creating a Character object and placing it in a room
emily = Character("Emily", "A friendly attendant")
emily.set_conversation("Would you like to have a drink?")
ballroom.set_character(emily)  # Placing Character object in Ballroom

# Creating an Enemy object (inherited from Character class) and placing it in a room
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("I would love to eat your insides...Aaaarrrgh")
dave.set_weakness("magic")
dining_hall.set_character(dave)

# Creating a Friend object (inherited from Character class) and placing it in a room
jack = Friend("Jack", "A jubilant detective")
jack.set_conversation("Be careful in the Dining Hall!!!")
jack.set_gift("Torchlight")
kitchen.set_character(jack)  # Placing Friend object in Ballroom

# Displaying room details
current_room = kitchen
current_room.get_details()
# Check if current room has any Character object
inhabitant = current_room.get_character()
if inhabitant is not None:
    inhabitant.describe()

dead = False
while not dead:
    print("\n")
    command = input("> ")
    # Command to move between rooms
    if command in ["north", "south", "west", "east"]:
        current_room, room_changed = current_room.move(command)
        if room_changed:
            current_room.get_details()
            inhabitant = current_room.get_character()
            if inhabitant is not None:
                inhabitant.describe()
    # Command to talk to the Character present in current room, if any present
    elif command == "talk":
        if inhabitant is not None and isinstance(inhabitant, Character):
            inhabitant.talk()
    # Command to fight the Character present in current room, provided it is an Enemy
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            print("What will you fight with?")
            fight_with = input()
            if not inhabitant.fight(fight_with):
                print("The game has ended!!!")
                dead = True  # results in 'while' loop and as a result, the game ending
        else:
            print("There is no character here to fight with!!!")
    # Command to receive a gift from the Character present in current room, provided it is a Friend
    elif command == "gift":
        if inhabitant is not None:
            if isinstance(inhabitant, Friend) and inhabitant.get_gift() is not None:
                inhabitant.receive_gift()
            elif isinstance(inhabitant, Friend) and inhabitant.get_gift() is None:
                print("This Friend has no gift sadly!")
            else:
                print("This character is not a Friend!")

