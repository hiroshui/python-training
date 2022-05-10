"""
Add 'docstrings' to the following functions and classes.
Make sure to follow the Python conventions.
"""
# Square the input
def square(number):
    """Return the square product of number."""
    return number * number

# Count the vowels of the input
def count_vowels(word):
    """Return the total number of vowels"""
    number_of_vowels = 0
    for char in word.lower():
        if char in "aeiou":
            number_of_vowels += 1
    return number_of_vowels

# Class of a dog
class Dog:
    """A class to represent a dog."""

    def __init__(self, name):
        """The default contructor of a dog"""
        self.name = name

    def bark(self):
        """Let the dog bark by saying whoof"""
        print(f"{self.name} says whoof!")

    def test(self):
        """Blabla"""
        print("Lorem ipsum doloret.")
