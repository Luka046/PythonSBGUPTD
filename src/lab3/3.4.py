def calculate_average(a, b, c):
    return (a + b + c) / 3

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))
average = calculate_average(a, b, c)
print(f"Среднее арифметическое: {average:.2f}")