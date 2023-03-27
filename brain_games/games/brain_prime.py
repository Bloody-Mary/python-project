from brain_games.scripts import utils
from random import randint
import math


GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
FIRST_NUM = 2
LAST_NUM = 50


def is_prime(num):
    x = math.sqrt(num)
    i = 2
    while i <= x:
        if num % i == 0:
            return False
        else:
            i += 1
    return True


def get_question_and_answer():
    question = randint(FIRST_NUM, LAST_NUM)
    correct_answer = utils.boolean_to_answer(is_prime(question))
    return correct_answer, question
