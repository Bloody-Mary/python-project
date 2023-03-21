from random import randint


GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
FIRST_NUM = 1
LAST_NUM = 100


def is_even(number):
    return number % 2 == 0


def get_question_and_answer():
    question = randint(FIRST_NUM, LAST_NUM)
    correct_answer = 'no'
    if is_even(question):
        correct_answer = 'yes'
        return correct_answer, question
    return correct_answer, question