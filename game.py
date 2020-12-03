# The start of a roguelike game, functions still need to be improved and expanded, eventually implemented into an actual game
class Item:
    def __init__(self, name, attribute, attack=False):
        # initialize instance item parameters
        self.name = name
        self.attribute = attribute
        self.attack = attack
    def __str__(self):
        # string which will be output to the player
        return "Item: " + self.name + "\nProperties: " + self.attribute + "\nAttack: " + str(self.attack) + "\n"
    # add/remove item from the player's inventory list
    def addInventory(self):
        inventory.append(str(self))
    def removeInventory(self):
        inventory.remove(str(self))
class Room:
    def __init__(self, length, width):
        # initialize instance parameters for the length and width of the room
        self.length = length
        self.width = width
    def __str__(self):
        # generates the room which is output to the user
        string = ""
        for i in range(self.length):
            for x in range(self.width):
                # check if the x position is on the last column
                if x != self.width-1:
                    # check if the position is a wall space
                    if i == 0 or x == 0 or i == self.length-1:
                        # door spaces are marked with "/"
                        if door[0] == x and door[1] == i:
                            string += "/"
                        else:
                            # wall spaces are marked with "X"
                            string += "X"
                    else:
                        # player space is marked with "@"
                        if playerpos[0] == x and playerpos[1] == i:
                            string += "@"
                        # other interior spaces are marked with "-"
                        else:
                            string += "-"
                else:
                    # finish every row in the room with either a wall space or a door space and a newline
                    if door[0] == x and door[1] == i:
                        string += "/\n"
                    else:
                        string += "X\n"
        return string
def listInventory():
    # function to list out the inventory list in a format more readable to the user
    string = ""
    for item in range(len(inventory)):
        string += inventory[item] + "======\n"
    return string
def addItem(item):
    # adds an item to inventory list
    # inventory has 5 slots
    if len(inventory) < 5:
        item.addInventory()
        return "You got the " + item.name + "."
    else:
        # if the inventory is full, the attempt to pick up another item fails
        return "You're carrying too much to pick up the " + item.name + "."
def removeItem(item):
    # if the item exists in the inventory list, remove it from inventory
    if str(item) in inventory:
        item.removeInventory()
        return "You dropped the " + item.name + "."
    else:
        # if no item exists in inventory, the attempt to remove it fails
        return "No such item \"" + item.name + "\" in inventory."
def Move(roomx, roomy):
    # function to modify the position of the player in a room
    # if the position being moved to is not a wall, modify the player position in the desired direction
    # FIXME: does not yet account for doors
    if cmd == "move north":
        if (y+1) >= roomy:
            return "A wall stands in your path."
        else:
            playerpos[1] += 1
    elif cmd == "move south":
        if (y-1) <= 1:
            return "A wall stands in your path."
        else:
            playerpos[1] -= 1
    elif cmd == "move east":
        if (x+1) >= roomx:
            return "A wall stands in your path."
        else:
            playerpos[0] += 1
    elif cmd == "move west":
        if (x-1) <= 1:
            return "A wall stands in your path."
        else:
            playerpos[0] -= 1
    else:
        # if the player specifies a direction not used by the program, the move fails and valid moves are listed
        return "Invalid direction. Valid directions include: north, south, east, west."
inventory = []
# sample items for testing
Torch = Item("Torch", "Lights up a 20 foot radius.")
Wooden_Sword = Item("Wooden Sword", "Does 2 damage.", 2)
# sample positions for testing
door = [7, 2]
playerpos = [2, 3]
Room1 = Room(8, 8)
# prints the test room
print(Room1)
