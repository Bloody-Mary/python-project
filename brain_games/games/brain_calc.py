from random import randint, choice
from operator import add, sub, mul


GAME_RULE = 'What is the result of the expression?'


def question_and_answer():
    num1 = randint(1, 50)
    num2 = randint(1, 50)
    operations = ['+', '-', '*']
    operation = choice(operations)
    if operation == '+':
        correct_answer = num1 + num2
    elif operation == '-':
        correct_answer = num1 - num2
    elif operation == '*':
        correct_answer = num1 * num2
    question = f"{num1} {operation} {num2}"
    return str(correct_answer), question
