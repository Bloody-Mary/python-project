from random import randint
import utils


GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
FIRST_NUM = 1
LAST_NUM = 100


def is_even(num):
    return num % 2 == 0


def get_question_and_answer():
    question = randint(FIRST_NUM, LAST_NUM)
    correct_answer = utils.boolean_to_answer(is_even(question))
    return correct_answer, question
