"""
This is an exercise to get familiar with Pylint.

You can install pylint with:
pip install pylint

To use pylint, run the following in the terminal/commandline:
pylint pylint_exercise.py
"""
#import statistics
#import os

# Main function
def main():
    """Main method"""
    name = input("What is your name? ")
    greet(name)

# Greeting function
def greet(name):
    """Greet someone with the given name and return 42"""
    local_variable = 42
    print(f"Hello {name}, how are you? Loc var: {local_variable}")
    return local_variable

# Make number to percentage
def make_percentage(number):
    """Calculate the percentages of the given number"""
    percentage = number / 100
    return f"{percentage}%"

if __name__ == "__main__":
    main()
