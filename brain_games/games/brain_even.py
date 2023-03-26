from random import randint
from brain_games.scripts import utils


GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
FIRST_NUM = 1
LAST_NUM = 100


def get_question_and_answer():
    question = randint(FIRST_NUM, LAST_NUM)
    rand_num = (num % 2 == 0)
    if utils.boolean_to_answer(rand_num) == True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, question
