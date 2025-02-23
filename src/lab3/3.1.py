import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

radius = float(input("Введите радиус круга: "))
area = calculate_circle_area(radius)
print(f"Площадь круга: {area:.2f}")