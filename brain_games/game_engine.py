import prompt

score = 3

def start_game(game_name):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?')
    print(f'Hello, {name}!')
    print(game_name.game_rule)
    counter = 0
    while counter < score:
        correct_answer, question = game_name.question_and_answer()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if not (answer == correct_answer):
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print("Let's try again, {name}!")
            break
        print('Correct!')
        counter += 1
    else:
        print(f'Congratulations, {name}!')
