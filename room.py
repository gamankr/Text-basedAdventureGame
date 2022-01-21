'''
Creating Room class and defining getter/setter methods
'''


class Room:
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}


    def set_name(self, room_name):
        self.name = room_name

    def get_name(self):
        return self.name

    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return self.description

    def describe(self):
        print(self.description)

    '''
    @param1 : the room object to link to
    @param2 : the relative direction of this object
    Usage: The room you are linking from is the object you call the method on, and the room you are linking 
    to is the object you pass into the method.
    '''
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        print(self.name, "Linked rooms: ", repr(self.linked_rooms))

    '''
    When entering a room in the game, the game displays a description of that room to the player using this method. 
    '''
    def get_details(self):
        print("The", self.name)
        print("----------------------")
        print(self.description)
        for direction, room in self.linked_rooms.items():
            print("The " + room.get_name() + " is " + direction)

    '''
    Method to allow the player to move between rooms.
    '''
    def move(self, direction):
        if direction in self.linked_rooms:
            # self.linked_rooms[direction].get_details()
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self

