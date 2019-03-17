class Room:
    def __init__(self, name):
        self.name = name
        self.description = None
        self.linked_room = []
        self.character = None
        self.item = None
        self.count = 0

    def set_description(self, description):
        self.description = description

    def link_room(self, room, direction):
        self.linked_room.append((room, direction))

    def set_character(self, character):
        self.character = character

    def set_item(self, item):
        self.item = item

    def get_character(self):
        return self.character

    def get_item(self):
        return self.item

    def move(self, direction):
        for room in self.linked_room:
            if direction == room[1]:
                self = room[0]
                return self
        else:
            print("There is no room on {}.".format(direction))
            return self

    def get_details(self):
        print("""{}
-------------------
{}""".format(self.name, self.description))
        for room in self.linked_room:
            print("The {} is {}".format(room[0].name, room[1]))

    def __repr__(self):
        return str([self.name, self.description, self.linked_room, self.character, self.item])


class Enemy:
    count = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.phrase = None
        self.weakness = None

    def set_conversation(self, phrase):
        self.phrase = phrase

    def set_weakness(self, weakness):
        self.weakness = weakness

    def describe(self):
        print("{} is here!".format(self.name))
        print(self.description)

    def talk(self):
        print("[{} says]: {}".format(self.name, self.phrase))

    def fight(self, item):
        if item == self.weakness:
            Enemy.count += 1
            print("You fend {} off with the {}".format(self.name, item))
            return True
        print("{} crushes you, puny adventurer!".format(self.name))
        return False

    def get_defeated(self):
        return Enemy.count


class Item:
    def __init__(self, name):
        self.name = name
        self.description = None

    def set_description(self, description):
        self.description = description

    def get_name(self):
        return self.name

    def describe(self):
        print("The [{}] is here - {}".format(self.name, self.description))
