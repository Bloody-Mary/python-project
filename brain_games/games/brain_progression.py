from random import randint


GAME_RULE = 'What number is missing in the progression?'
PROG_STEP = randint(1, 9)
NUM_FIRST = randint(1, 10)
PROGRESSION_LEN = 10


def make_progression():
    global NUM_FIRST
    global PROG_STEP
    result = []
    hidden = randint(0, PROGRESSION_LEN - 1)
    last_num = NUM_FIRST
    for _ in range(PROGRESSION_LEN):
        next_number = last_num + PROG_STEP
        last_num = next_num
        result.append(next_num)
    return result, hidden


def get_question_and_answer():
    result, hidden = make_progression()
    correct_answer = result.pop(hidden)
    result.insert(hidden, "..")
    question = " ".join(map(str, result))
    return str(correct_answer), question
