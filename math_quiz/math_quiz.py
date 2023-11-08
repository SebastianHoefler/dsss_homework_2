import random


def random_integer(min:int, max:int):
    """
    Generate a random integer between 'min' and 'max' boundries included.

    Parameters:
    min (int): The lower bound of the random number range.
    max (int): The upper bound of the random number range.

    Returns:
    int: A random integer between 'min' and 'max'.

    Raises:
    ValueError: If 'min' is greater than 'max'.
    TypeError: If 'min' or 'max' are not integers
    """

    if min > max:
        raise ValueError('min should not be greater than max')
    
    if type(min) is not int:
        raise TypeError('min should be an integer')

    if type(max) is not int:
        raise TypeError('max should be an integer')

    return random.randint(min, max)


def random_operator():
    '''
    Generates a random operator from the choice (+, -, *)

    Parameters: None

    Returns:
    str: One of the following operators: '+', '-', '*'
    '''
    return random.choice(['+', '-', '*'])


def create_problem(n1, n2, o):
    """
    Generate a math problem and its solution.

    Parameters:
    n1 (int/float): First number.
    n2 (int/float): Second number.
    o (str): Operator ('+', '-', '*').

    Returns:
    (str, int/float): A tuple with the problem and the answer.

    Examples:
    $ create_problem(1, 2, '+')
    ('1 + 2', 3)
    """
    p = f"{n1} {o} {n2}"
    if o == '+': a = n1 + n2
    elif o == '-': a = n1 - n2
    elif o == '*': a = n1 * n2
    return p, a


def math_quiz():
    """
    Starts the math test with random problems

    total_questions is a hyperparameter that can be set within this function.

    No parameters. Final score is displayed at the end of the quiz.
    """
    score = 0
    total_questions = 3  # Total number of questions in the quiz

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = random_integer(1, 10)
        num2 = random_integer(1, 10)
        op = random_operator()

        problem, answer = create_problem(num1, num2, op)
        print(f"\nQuestion: {problem}")

        try:
            user_answer = int(input("Your answer: "))
            if user_answer == answer:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {answer}.")
        except ValueError:
            print("Invalid input. Please enter a numeric answer.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
