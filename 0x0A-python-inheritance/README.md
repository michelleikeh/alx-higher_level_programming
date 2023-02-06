# Python - Inheritance

In this project, I learned about Python class inheritance. I learned about the
differences between super- and sub-classes while practicing inheritance,
definining classes with multiple base classes, and overiding inherited methods
and attributes.

## Technologies
* Python Scripts are written with Python 3.8.*`
* Tested on Ubuntu 20.04 LTS

## Tests :heavy_check_mark:

* [tests](./tests): Folder of test files. Includes both ALX-provided ones
as well as the following two independently-developed:
    * [1-my_list.txt](./1-my_list.txt)
    * [7-base_geometry.txt](./7-base_geometry.txt)

## Function Prototypes :floppy_disk:

Prototypes for functions written in this project:

| File                    | Prototype                             | Description                              |
| ----------------------- | ------------------------------------- |------------------------------------------|
| `0-lookup.py`           | `def lookup(obj):`                    |Function that returns the list of available attributes and methods of an object |
| `1-my_list.py`          |                                       | Class `MyList` that inhertis from `list` |
| `2-is_same_class.py`    | `def is_same_class(obj, a_class):`    | Function that returns `True` if the object is exactly an instance of the specified class; otherwise `False` |
| `3-is_kind_of_class.py` | `def is_kind_of_class(obj, a_class):` |Function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class |
| `4-inherits_from.py`    | `def inherits_from(obj, a_class):`    | Function that returns `True` if the object is an instance of a class that inherited from the specified class |
| `5-base_geometry.py` |                                     | Empty class `BaseGeometry` |
| `6-base_geometry.py` |   |Class `BaseGeometry` with public instance method `def area(self):` |
| `7-base_geometry.py` |   |Class `BaseGeometry` with public instance method that verifies if the input arg is an integer |
| `8-rectangle.py` |   |Class `Rectangle` that inhertis from `BaseGeometry` |
| `9-rectangle.py` | |Class `Rectangle` that inhertis from `BaseGeometry`, with `area()` method implemented |
| `10-square.py` |  | Class `Square` that inherits from `Rectangle` |
| `11-square.py` || Class `Square` that inherits from `Rectangle`, with `str()` method |
| `100-my_int.py` || Class `MyInt` that inhertis from `int`. Its `==` and `!=` operators are inverted |
| `101-add_attribute.py`  | `def add_attribute(obj, att, value):` ||


