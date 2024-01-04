class Rectangle:
    def __init__(self, width, height):
        # Initialize the width and height attributes using the setter methods
        self.width = width
        self.height = height

    @property
    def width(self):
        # Getter method for the 'width' property
        return self.__width

    @width.setter
    def width(self, value):
        # Check if the provided value is an integer
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        # Check if the value is greater than 0
        if value < 0:
            raise ValueError("width should be > 0")

        # Set the value of the private attribute '__width'
        self.__width = value

    @property
    def height(self):
        # Getter method for the 'height' property
        return self.__height

    @height.setter
    def height(self, value):
        # Check if the provided value is an integer
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        # Check if the value is greater than 0
        if value < 0:
            raise ValueError("height should be > 0")

        # Set the value of the private attribute '__height'
        self.__height = value
