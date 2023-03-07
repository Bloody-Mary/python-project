from random import randint


game_rule = 'What number is missing in the progression?'


def progression_gen():
    prog_step = randint(1, 9)
    num_first = randint(1, 10)
    stop = num_first + (prog_step * 10)
    progression = [str(x) for x in range(num_first, stop, prog_step)]
    return progression


def question_and_answer():
    progression = progression_gen()
    skip = randint(0, 9)
    correct_answer = progression[skip]
    progression[skip] = '..'
    question = " ".join(progression)
    return correct_answer, question
