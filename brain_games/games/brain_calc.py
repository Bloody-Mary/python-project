from random import randint, choice


game_rule = 'What is the result of the expression?'


def question_and_answer():
    num1 = randint(0, 50)
    num2 = randint(0, 50)
    operations = ('+', '-', '*')
    calc_operation = choice(operations)

    operations = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
    }
    correct_answer = operations[calc_operation]
    question = f"{num1} {calc_operation} {num2}"
    return correct_answer, question
