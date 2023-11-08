# Contents of your_package/__init__.py

print("your_package has been imported")

__all__ = ["math_quiz", "tests_math_quiz"]

from . import math_quiz
from . import tests_math_quiz