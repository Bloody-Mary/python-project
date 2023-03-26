from random import randint
from brain_games.scripts import utils


GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
FIRST_NUM = 1
LAST_NUM = 100


def is_even(number):
    return number % 2 == 0


def get_question_and_answer():
    question = randint(FIRST_NUM, LAST_NUM)
    if is_even(question) == True:
        return utils.boolean_to_answer(correct_answer)
    elif is_even(question) == False:
        return utils.boolean_to_answer(correct_answer)
    return correct_answer, question
