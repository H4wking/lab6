class Furniture():
    """
    Class for Furniture representation.
    """
    def __init__(self, style, assign):
        self.style = style
        self.assign = assign

    def __str__(self):
        """
        (Furniture) -> str
        :return: string representation of Furniture object.
        """
        return "<furniture style is {}>".format(self.style)


class Chair(Furniture):
    """
    Class for chair representation.
    """
    def __init__(self, style, assign, tipe):
        super().__init__(style, assign)
        self.tipe = tipe

    def __str__(self):
        """
        (Chair) -> str
        :return: string representation of Chair object.
        """
        return "<This {} furniture style is {}>".format(self.tipe, self.style)

    def get_assign(self):
        """
        (Chair) -> str
        :return: location of Chair object.
        """
        return self.assign


if __name__ == "__main__":
    furniture1 = Furniture("empire", "bedroom")
    furniture2 = Furniture("modern", "bathroom")
    assert (not (furniture1 == furniture2))
    assert (furniture1.style == "empire")
    assert (furniture1.assign == "bedroom")
    assert (str(furniture1) == "<furniture style is empire>")
    chair1 = Chair("empire", "bedroom", "armchair")
    assert (chair1.tipe == "armchair")
    assert (isinstance(chair1, Furniture))
    assert (str(chair1) == "<This armchair furniture style is empire>")
    assert (chair1.get_assign() == "bedroom")
