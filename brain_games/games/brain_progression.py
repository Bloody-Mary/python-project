from random import randint


GAME_RULE = 'What number is missing in the progression?'


def make_progression():
    PROG_STEP = randint(1, 9)
    NUM_FIRST = randint(1, 10)
    PROGRESSION_STEP = randint(5, 10)
    result = []
    for _ in range(PROGRESSION_STEP):
        next_number = num_first + prog_step
        result.append(next_number)
        num_first = next_number
    return result


def get_question_and_answer():
    result = make_progression()
    hidden = randint(0, len(PROGRESSION_STEP) - 1)
    correct_answer = result[hidden]
    result[hidden] = '..'
    question = ' '.join(str(x) for x in result)
    return str(correct_answer), question
