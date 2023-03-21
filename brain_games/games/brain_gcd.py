from random import randint
import math


GAME_RULE = 'Find the greatest common divisor of given numbers.'
FIRST_NUM = 0
LAST_NUM = 50


def get_question_and_answer():
    num1 = randint(FIRST_NUM, LAST_NUM)
    num2 = randint(FIRST_NUM, LAST_NUM)
    correct_answer = math.gcd(num1, num2)
    question = f'{num1} {num2}'
    return str(correct_answer), question