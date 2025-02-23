def is_divisible_by_3(number):
    return number % 3 == 0

number = int(input("Введите число: "))
if is_divisible_by_3(number):
    print(f"Число {number} делится на 3")
else:
    print(f"Число {number} не делится на 3")