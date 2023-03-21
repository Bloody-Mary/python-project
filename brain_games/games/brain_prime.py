from random import randint


GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
FIRST_NUM = 2
LAST_NUM = 50


def is_prime(num):
    for hidden_num in range(2, num // 2 + 1):
        if num % hidden_num == 0:
            return True


def get_question_and_answer():
    question = randint(FIRST_NUM, LAST_NUM)
    correct_answer = 'yes'
    if is_prime(question):
        correct_answer = 'no'
        return correct_answer, question
    return correct_answer, question