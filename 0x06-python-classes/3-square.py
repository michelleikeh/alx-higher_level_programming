#!/usr/bin/python3
"""Module containing the Square class"""

class Square:
    """ defines a Square. """
   
   def __init__(self, size=0):
        """ Initialize a new square.

        Args:
            size(int): the size of the new square.
        """
   
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Return the area of the square. """
   
        return (self.__size * self.__size)
