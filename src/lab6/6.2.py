def divide_100_by_number():
    try:
        number = int(input("Введите число: "))
        result = 100 / number
        print(f"Результат: {result}")
    except ValueError:
        print("Ошибка: введено не число")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

divide_100_by_number()