from random import randint
import math


GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


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
    num = randint(1, 50)
    if not is_prime(num):
        correct_answer = 'no'
    else:
        correct_answer = 'yes'
    return correct_answer, question
