from random import randint


GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
RAND_NUM = randint(1, 100)


def is_even(number):
    answer = {True: 'yes', False: 'no'}
    if number % 2 == 0:
        return ANSWER[True]
    else:
        return ANSWER[False]


def get_question_and_answer():
    question = RAND_NUM
    correct_answer = is_even(question)
    return correct_answer, question
