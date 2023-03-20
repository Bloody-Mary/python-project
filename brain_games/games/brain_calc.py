from random import randint, choice


GAME_RULE = 'What is the result of the expression?'
OPERATIONS = ('+', '-', '*')


def operation_choice(operation, num1, num2):
    if operation == '+':
        correct_answer = num1 + num2
    elif operation == '-':
        correct_answer = num1 - num2
    elif operation == '*':
        correct_answer = num1 * num2
    return correct_answer


def get_question_and_answer():
    num1 = randint(1, 50)
    num2 = randint(1, 50)
    operation = choice(OPERATIONS)
    question = f"{num1} {operation} {num2}"
    correct_answer = str(operation_choice(operation, num1, num2))
    return correct_answer, question
