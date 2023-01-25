#!/usr/bin/python3
"""Module containing the Square class"""


class Square:
    """ Represent a square. """
    
    def __init__(self, size=0):
        """Initialie a new square.

        Args:
            size(int): the size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns area of square """
        return(self.__size * self.__size)

    @property
    def size(self):
        """Get/set the set of the square """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ Set the size value """
        if not isinstance(value, int):
            raise TypeError("size must be integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
