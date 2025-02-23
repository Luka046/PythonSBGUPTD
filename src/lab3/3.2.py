def solve_linear_equation(a, b):
    if a == 0:
        return "Уравнение не имеет решения"
    return -b / a

a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
x = solve_linear_equation(a, b)
print(f"Решение уравнения: x = {x}")