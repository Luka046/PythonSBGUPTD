def celsius_to_fahrenheit(celsius):
    return (9 / 5) * celsius + 32

celsius = float(input("Введите температуру в градусах Цельсия: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"Температура в градусах Фаренгейта: {fahrenheit:.2f}")