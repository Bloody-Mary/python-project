from random import randint


GAME_RULE = 'What number is missing in the progression?'
FIRST_NUM = 1
END_RANGE = 9
END_STEP = 10
PROGRESSION_LEN = 10


def make_progression():
    num_first = randint(FIRST_NUM, END_RANGE)
    prog_step = randint(FIRST_NUM, END_STEP)
    result = []
    hidden = randint(0, PROGRESSION_LEN - 1)
    last_num = num_first
    for _ in range(PROGRESSION_LEN):
        next_num = last_num + prog_step
        last_num = next_num
        result.append(next_num)
    return result, hidden


def get_question_and_answer():
    result, hidden = make_progression()
    correct_answer = result.pop(hidden)
    result.insert(hidden, "..")
    question = " ".join(map(str, result))
    return str(correct_answer), question