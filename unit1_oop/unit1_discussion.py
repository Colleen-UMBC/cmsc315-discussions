"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class Film:
    # Include at least one class variable
    media_type = "Film"

    # Include a constructor (__init__)
    def __init__(self, title: str, release_date: int):
        # Include at least two instance variables
        self._title = title
        self._release_date = release_date

    # Include a method that returns or displays information about the object
    def display_info(self):
        print(f"Media Type: {self.media_type}")
        print(f"Title: {self._title}")
        print(f"Release Date: {self._release_date}")


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class Documentary(Film):
    # Add at least one new class variable
    film_genre = "Documentary"

    def __init__(self, title: str, release_date: int, topic: str, publisher: str):
        # Use inheritance
        super().__init__(title, release_date)

        # Add at least two new instance variables
        self._topic = topic
        self._publisher = publisher
        self.cast = []

    # Override a method from the parent class
    def display_info(self):
        print(f"Film Genre: {self.film_genre}")
        print(f"Title: {self._title}")
        print(f"Release Date: {self._release_date}")
        print(f"Topic: {self._topic}")
        print(f"Publisher: {self._publisher}")
        print(f"Cast: {', '.join(self.cast)}")

    # Add at least one new method
    def add_cast_member(self, cast_name: str):
        self.cast.append(cast_name)



# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    print("TODO: Implement namespace demonstration")

    # Create at least two objects of the child class
    doc1 = Documentary("March of the Penguins", 2005, "Animals", "National Geographic")
    doc2 = Documentary("My Octopus Teacher", 2020, "Animals", "Netflix")

    # Access a class variable through the class itself
    print(f"Class Variable through the class itself: {Documentary.film_genre}")

    # Access the same class variable through an object
    print(f"Class Variable through an object: {doc1.film_genre}")

    # Add a new attribute to only one object after it is created
    doc1.director = "Luc Jacquet"

    # Display each object's namespace using __dict__
    # Instance namespace: "Manages attributes specific to an individual object"
    # Taken from 2.8 of textbook
    print(f"Documentary 1 namespace: {doc1.__dict__}")
    print(f"Documentary 2 namespace: {doc2.__dict__}")

    # Display information about the class namespace
    # Class namespace: "manages members that are to be shared by all instances of a class"
    # Taken from 2.8 of textbook
    print(f"Class namespace: {Documentary.__dict__}")



# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    print("TODO: Implement shallow copy and deep copy demonstration")

    # Create an object that contains nested mutable data
    doc3 = Documentary("Apollo 11", 2019, "History", "Neon")
    doc3.add_cast_member("Neil Armstrong")
    doc3.add_cast_member("Mike Collins")

    # Create a shallow copy
    # "Distinct lists [but] there remains indirect aliasing"
    # Taken from 2.9.2 of the textbook
    doc3_shallow = copy(doc3)

    # Create a deep copy
    # "References its own copies of those objects referenced by the original version"
    # Taken from 2.9.2 of the textbook
    doc3_deep = deepcopy(doc3)

    # Modify the original object's nested data
    doc3.cast[0] = "Buzz Aldrin"

    # Display the original object, shallow copy, and deep copy
    print("\n=== Original Object ===")
    doc3.display_info()
    print("\n=== Shallow Copy ===")
    doc3_shallow.display_info()
    print("\n=== Deep Copy ===")
    doc3_deep.display_info()



# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    # Create at least one object from the parent class
    # Demonstrate inheritance by calling methods
    print("\nTODO: Create and test your parent object")
    film1 = Film("Midsommar", 2019)
    film1.display_info()

    # Create at least one object from the child class
    # Demonstrate inheritance by calling methods
    print("\nTODO: Create and test your child object")
    doc4 = Documentary("Prophet's Prey", 2015, "Cults", "Showtime")
    doc4.display_info()

    # Call your namespace demonstration function
    # Call your copy demonstration function
    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()