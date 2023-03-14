from random import randint, choice


GAME_RULE = 'What is the result of the expression?'
NUM1 = randint(1, 50)
NUM2 = randint(1, 50)
OPERATIONS = ('+', '-', '*')


def operation_choice(operation, NUM1, NUM2):
    if operation == '+':
        correct_answer = NUM1 + NUM2
    elif operation == '-':
        correct_answer = NUM1 - NUM2
    elif operation == '*':
        correct_answer = NUM1 * NUM2
    return correct_answer


def get_question_and_answer():
    operation = choice(OPERATIONS)
    question = f"{NUM1} {operation} {NUM2}"
    return correct_answer, question
