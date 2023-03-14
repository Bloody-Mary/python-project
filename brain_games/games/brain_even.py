from random import randint


GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
RAND_NUM = randint(1, 100)
ANSWER = {True: 'yes', False: 'no'}


def bool_answer(number):
    if number % 2 == 0:
        return ANSWER[True]
    else:
        return ANSWER[False]


def get_question_and_answer():
    question = str(RAND_NUM)
    correct_answer = bool_answer(question)
    return correct_answer, question
