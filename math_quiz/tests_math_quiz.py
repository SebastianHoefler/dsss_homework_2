import unittest
from math_quiz import random_integer, random_operator, create_problem

class TestMathGame(unittest.TestCase):

    def test_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator(self):
        # Test if the random operator is one of '+', '-', '*'
        for _ in range(1000):  # Test a large number of random operators
            op = random_operator()
            self.assertIn(op, ['+', '-', '*'])

    def test_create_problem(self):
        # Test if create_problem function creates the correct problem and answer
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (10, 3, '-', '10 - 3', 7),
            (4, 6, '*', '4 * 6', 24),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = create_problem(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)


if __name__ == "__main__":
    unittest.main()
