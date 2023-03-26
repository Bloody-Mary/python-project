from random import randint
from brain_games.scripts import utils


GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
FIRST_NUM = 1
LAST_NUM = 100
SOME_VAR = True


def is_even(number):
    if number % 2 == 0:
        return utils.boolean_to_answer(SOME_VAR)


def get_question_and_answer():
    question = randint(FIRST_NUM, LAST_NUM)
    correct_answer = is_even(question)
    return str(correct_answer), question
