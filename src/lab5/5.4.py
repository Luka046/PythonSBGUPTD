import random

def math_game():
    correct_answers = 0
    mistakes = 0

    while mistakes < 3:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        answer = input(f"{a} + {b} = ")

        if answer.isdigit() and int(answer) == a + b:
            print("Правильно!")
            correct_answers += 1
        else:
            print("Ответ неверный")
            mistakes += 1

    print(f"Игра окончена. Правильных ответов: {correct_answers}")

math_game()