from room import Room
from character import Character

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

# Displaying room details
current_room = kitchen
current_room.get_details()
# Check if current room has any Character object
inhabitant = current_room.get_character()
if inhabitant is not None:
    inhabitant.describe()

while True:
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

