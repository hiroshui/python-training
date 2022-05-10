"""
Type hinting exercise
"""
from typing import List, Union, Dict

def main():
    """Simple program for illustrative purposes"""
    age : int = ask_user_age()
    print_age(age)

def ask_user_age() -> int:
    """Return user input"""
    age : int = input("What is your age in years? ")
    return int(age)

def print_age(age : int):
    """Print full sentence"""
    age_in_months : int = age * 12
    print(f"You are {age_in_months} months old.")


def get_list() -> List[Union[int,float]]:
    y : List[Union[int,float]] = [0, 1, 2.0, 4.3]
    return y

def get_dic() -> Dict[int, List[str]]:
    z : Dict[int, List[str]] = {1: {"name": "Jane"}, 2: {"name": "John"}}
    return z

if __name__ == "__main__":
    #main()
    #print(get_list())
    print(get_dic()[1])