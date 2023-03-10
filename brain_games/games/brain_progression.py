from random import randint


GAME_RULE = 'What number is missing in the progression?'


def question_and_answer():
    prog_step = randint(1, 9)
    num_first = randint(1, 10)
    progression = randint(5, 10)
    
    result = []
    i = 0
    while i < progression:
        result.append(num_first + prog_step * i)
        i += 1
    hidden = randint(0, progression - 1)
    correct_answer = result[hidden]
    result[hidden] = '..'
    question = ' '.join(str(x) for x in result)
    return str(correct_answer), question
