from random import randint

game_rule = 'Answer "yes" if the number is even, otherwise answer "no".'

def question_and_answer():
    rand_num = randint(1, 100)
    question = str(rand_num)
    if rand_num % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, question
