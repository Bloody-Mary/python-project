from random import randint


GAME_RULE = 'What number is missing in the progression?'


def make_progression(min_num, max_num, min_step, max_step, prog_len):
    num_first = randint(min_num, max_num)
    prog_step = randint(min_step, max_step)
    result = [num_first, ]
    for _ in range(prog_len):
        next_number = num_first + prog_step
        result.append(next_number)
        num_first = next_number
    return result


def get_question_and_answer():
    result = make_progression(min_num = 1,
            max_num = 10,
            min_step = 1,
            max_step = 30,
            prog_len = 10)
    hidden = randint(0, len(progression_step) - 1)
    correct_answer = result[hidden]
    result[hidden] = '..'
    question = ' '.join(str(x) for x in result)
    return str(correct_answer), question
