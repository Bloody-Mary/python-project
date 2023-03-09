from random import randint
import math


game_rule = 'Find the greatest common divisor of given numbers.'


def question_and_answer():
    num1 = randint(0, 50)
    num2 = randint(0, 50)

    correct_answer = math.gcd(num1, num2)
    question = f'{num1} {num2}'
    return str(correct_answer), question
