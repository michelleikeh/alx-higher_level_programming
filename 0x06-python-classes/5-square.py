#1/usr/bin/python3
"""Module containing the Square class"""
class Square:
    """Define s a square class """
    def __init__(size, size=0):
        """Initialize a square object """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Return the area of the square"""
        return (self.__size ** 2)

    @property
    def size(self):
        """ return the size value """
        return self.__size

    @size.setter
    def size(self, value):
        """sets the value of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """ prints a # square according
        to the size value
        """
        if not self.__size:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()
