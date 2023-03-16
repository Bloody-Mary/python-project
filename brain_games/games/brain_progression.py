from random import randint


GAME_RULE = 'What number is missing in the progression?'
prog_step = randint(1, 9)
num_first = randint(1, 10)
progression_step = randint(5, 10)


def make_progression():
    global num_first
    global prog_step
    result = []
    for _ in range(progression_step):
        next_number = num_first + prog_step
        result.append(next_number)
        num_first = next_number
    return result


def get_question_and_answer():
    result = make_progression()
    hidden = randint(0, len(result) - 1)
    correct_answer = result[hidden]
    result[hidden] = '..'
    question = ' '.join(str(x) for x in result)
    return question, str(correct_answer)
