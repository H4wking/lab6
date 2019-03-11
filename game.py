class Room:
    def __init__(self, name):
        self.name = name
        self.description = None
        self.linked_room = []
        self.character = None
        self.item = None

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
                opposite = ""
                if direction == "north":
                    opposite = "south"
                elif direction == "south":
                    opposite = "north"
                elif direction == "west":
                    opposite = "east"
                elif direction == "east":
                    opposite = "west"
                self.linked_room.append((self, opposite))
                self.name = room[0].name
                self.description = room[0].description
                self.linked_room = room[0].linked_room
                self.character = room[0].character
                self.item = room[0].item
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


    def __str__(self):
        return str([self.name, self.description, self.linked_room, self.character, self.item])


class Enemy:
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
        print(self.description)

    def talk(self):
        print(self.phrase)


class Item:
    def __init__(self, name):
        self.name = name
        self.description = None

    def set_description(self, description):
        self.description = description

    def get_name(self):
        return self.name

    def describe(self):
        print(self.description)
