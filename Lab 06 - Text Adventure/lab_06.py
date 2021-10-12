class Room:

    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west

def main():
    # Bathroom
    room_list = []
    room = Room("""You have entered the bathroom. The water from the shower is almost flooding the bathroom.
                You move out of the bathroom so your socks and shoes don't get soaked.
                There is a door to the south.""", None, None, 3, None)
    room_list.append(room)
    # North hallway
    room = Room("""You have entered the north hallway.
                This hallway is long, narrow, and dirt is all over the walls.
                There is a door to the east, south, and west. Choose wisely!""", None, 2, 5, 3)
    room_list.append(room)
    # First bedroom
    room = Room("""You have entered the first bedroom. 
                 In the first bedroom you see the curtains by the window swirling everywhere,
                 even though the windows are closed.
                 There is a door to the west.""", None, None, None, 1)
    room_list.append(room)
    # Second bedroom
    room = Room("""You have entered the second bedroom.
                 In the second bedroom you experience the same unsafe feeling in the first bedroom,
                 but the clothes from the dressers are spread out everywhere.
                 Also, some of your belongings are missing!
                 There is a door to the north and east. What are you gonna choose?""", 0, 1, None, None)
    room_list.append(room)
    # Living room
    room = Room("""You have entered the living room.
                 When you enter the living room everything seems normal,
                 but as you approach the couch to sit down you here a noise.
                 The noise is screaming coming from the hallway.
                 There is a door to the east. 
                 Must use that door to go into another room.""", None, 5, None, None)
    room_list.append(room)
    # South hallway
    room = Room("""You have entered the south hallway.
                 The screaming gets louder which means you are getting closer,
                 but don't see what/who is screaming.
                 There is a door to the north, east, and west. Choose wisely!""", 1, 6, None, 4)
    room_list.append(room)
    # Kitchen
    room = Room("""You have entered the kitchen."
                 As you walk into the kitchen you see the whole place is a huge mess.
                 The screaming suddenly stops. You are very confused and not sure what is going on.
                 As you look out the window you see it and what all the screaming is about.
                 There is a door to the west. 
                 It looks like that is the door you will choose.""", None, None, None, 5)
    room_list.append(room)

    current_room = 0

    done = False
    while not done:
        print(room_list[current_room].description)
        print()
        user_input = input("What would you like to choose?")
        if user_input.lower() == "n" or user_input.lower() == "north":
            next_room = room_list[current_room].north
            if next_room == None:
                print("You can't go that way. Game over! Restart game.")
            current_room = next_room

        elif user_input.lower() == "e" or user_input.lower() == "east":
            next_room = room_list[current_room].east
            if next_room == None:
                print("You can't go that way. Game over! Restart game.")
            current_room = next_room

        elif user_input.lower() == "s" or user_input.lower() == "south":
            next_room = room_list[current_room].south
            if next_room == None:
                print("You can't go that way. Game over! Restart game.")
            current_room = next_room

        elif user_input.lower() == "w" or user_input.lower() == "west":
            next_room = room_list[current_room].west
            if next_room == None:
                print("You can't go this way. Game over! Restart game.")
            current_room = next_room

main()