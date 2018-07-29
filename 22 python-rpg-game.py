def showInstruction():
    #print a main menu and the commands
    print("RPG Game")
    print("========")
    print("Commands:")
    print("'inventory'")
    print("'go [direction]'")
    print("'look'")
    print("'take [item]'")
    print("'place' [item]'")
    print("Note: no error checking")

def showStatus():
    #print the player's current status
    print("---------------------------")
    print("You are in the " + rooms[currentRoom]["name"])
    print("---------------------------")

rooms = {
            1 : {   "name"  : "Hall",
                    "north" : 0,
                    "east"  : 2,
                    "south" : 3,
                    "west"  : 0,
                    "item"  : "boots" },

            2 : {   "name"  : "Bedroom",
                    "north" : 0,
                    "east"  : 0,
                    "south" : 4,
                    "west"  : 1,
                    "item"  : "lantern" },

            3 : {"name"  : "Kitchen",
                    "north" : 1,
                    "east"  : 0,
                    "south" : 0,
                    "west"  : 0,
                    "item"  : "knife" },

            4 : {   "name"  : "Bathroom",
                    "north" : 2,
                    "east"  : 0,
                    "south" : 0,
                    "west"  : 0,
                    "item"  : "none" }
}

currentRoom = 1

inventory = []

showInstruction()

bull = True

while bull:
    showStatus()

    move = input(">").lower().split()

    if move[0] == "inventory":
        if inventory != "":
            print("You have the following: " + str(inventory))
        else:
            print("You aren't carrying anything.")
    elif move[0] == "go":
        if rooms[currentRoom][move[1]] != 0:
            currentRoom = rooms[currentRoom][move[1]]
            print("Now in room " + rooms[currentRoom]["name"])
        else:
            print("Cannot go that direction")
    elif move[0] == "look":
        print("You are in the " + rooms[currentRoom]["name"] + ". There is a " + rooms[currentRoom]["item"] + " here.")
    elif move[0] == "take":
        if move[1] == rooms[currentRoom]["item"]:
            inventory.append(rooms[currentRoom]["item"])
            print("Picked up the " + rooms[currentRoom]["item"])
            rooms[currentRoom]["item"] = ""
        else:
            print("No such item")
    elif move[0] == "place":
        print("Not yet implemented")
    elif move[0] == "quit":
        bull = False