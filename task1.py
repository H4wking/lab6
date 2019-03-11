class Building():
    """
    Class for building representation.
    """
    def __init__(self, building, address):
        self.building = building
        self.address = address


class House(Building):
    """
    Class for house representation.
    """
    def __init__(self, building, address, apartments_list):
        super().__init__(building, address)
        self.apartments_list = apartments_list


class AcademicBuilding(Building):
    """
    Class for academic building representation.
    """
    def __init__(self, address, classrooms):
        super().__init__(address)
        self.classrooms = classrooms

    def total_equipment(self):
        """
        (AcademicalBuilding) -> lst
        :return: list of all the equipment in building.
        """
        equipment = []
        for i in self.classrooms:
            for j in i.equipment:
                 equipment.append(j)
        equipment_dict = {}
        for i in equipment:
            if i not in equipment_dict:
                equipment_dict[i] = 1
            else:
                equipment_dict[i] += 1
        equipment_count = []
        for i in equipment_dict:
            equipment_count.append((i, equipment_dict[i]))
        return equipment_count

    def __str__(self):
        """
        (AcademicalBuilding) -> str
        :return: string representation of building.
        """
        address = self.address + "\n"
        classrooms = ""
        for classroom in self.classrooms:
            classrooms += "Classroom {} has a capacity of {} persons and \
has the following equipment: {}.".format(classroom.number, classroom.capacity, ", ".join(classroom.equipment)) + "\n"
        return address + classrooms
