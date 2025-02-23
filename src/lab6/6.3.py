def is_magic_date(date):
    day, month, year = map(int, date.split('.'))
    return day * month == year % 100

date = input("Введите дату в формате ДД.ММ.ГГГГ: ")
if is_magic_date(date):
    print("Дата магическая!")
else:
    print("Дата не магическая.")