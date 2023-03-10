from random import randint
import math


GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime_number(num):
    x = math.sqrt(num)
    i = 2
    while i <= x:
        if num % i == 0:
            return False
        else:
            i += 1
    return True


def question_and_answer():
    question = randint(1, 50)
    correct_answer = 'yes' if prime_number(question) else 'no'
    return str(correct_answer), question
