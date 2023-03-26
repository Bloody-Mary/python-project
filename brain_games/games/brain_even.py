from random import randint
from brain_games.scripts import utils


GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
FIRST_NUM = 1
LAST_NUM = 100


def is_even(number):
    if number % 2 == 0:
        return correct_answer == True


def get_question_and_answer():
    question = randint(FIRST_NUM, LAST_NUM)
    correct_answer = True
    if is_even(question):
        return utils.boolean_to_answer(correct_answer)
    return str(correct_answer), question
