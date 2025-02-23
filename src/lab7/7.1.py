numbers = [10, 20, 30, 40, 50]
user_number = int(input("Введите число: "))

if user_number in numbers:
    print(f"Поздравляю, Вы угадали число {user_number}!")
else:
    print("Нет такого числа!")