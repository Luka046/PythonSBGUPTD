def determine_seat_type(seat_number):
    if seat_number < 1 or seat_number > 54:
        return "Неверный номер места"
    if seat_number % 2 == 0:
        return "Верхнее место"
    else:
        return "Нижнее место"

seat_number = int(input("Введите номер места: "))
print(determine_seat_type(seat_number))