# test_mathematics.py
from mathematics import hypotenuse, multiply, divide, round_up

def test_multiplication():
    assert multiply(4, 5) == 20

def test_division():
    assert divide(4, 5) == 0.8

def test_round_up():
    assert round_up(2.4) == 3

# second divison test
def test_division_second():
    assert divide(2, 3) == 0.7

def test_hypotenuse():
    """Returns the longest side of a right-angled triangle.

    Pythagorean Theorem: a² + b² = c²

            |\
          L | \
          e |  \ Hypotenuse (C)
          g |   \
         (A)|    \
            ------
            Leg(B)

    3² + 4² = 5²
    9  + 16 = 25
    Hypotenuse (c) = 5.0
    """
    assert hypotenuse(3, 4) == 5
    
def test_hypotenuse():
    """Returns the longest side of a right-angled triangle.

    Pythagorean Theorem: a² + b² = c²

            |\
          L | \
          e |  \ Hypotenuse (C)
          g |   \
         (A)|    \
            ------
            Leg(B)

    3² + 4² = 5²
    9  + 16 = 25
    Hypotenuse (c) = 5.0
    """
    assert hypotenuse(2, 5) == 5.39