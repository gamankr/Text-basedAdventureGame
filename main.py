from room import Room

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

current_room = kitchen
while True:
    print("\n")
    current_room.get_details()
    command = input("> ")
    # Command to move between rooms
    current_room = current_room.move(command)

