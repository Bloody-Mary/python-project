from random import randint
import math


GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
QUESTION = randint(1, 50)
ANSWER = {True: 'yes', False: 'no'}

def prime_number(num):
    x = math.sqrt(num)
    i = 2
    while i <= x:
        if num % i == 0:
            return False
        else:
            i += 1
    return True


def bool_answer(QUESTION):
    if prime_number(QUESTION):
        return ANSWER[True]
    else:
        return ANSWER[False]


def get_question_and_answer():
    correct_answer = str(bool_answer(QUESTION))
    return str(correct_answer), question
