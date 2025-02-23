def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return f"Год {year} - високосный"
    else:
        return "Это год не високосный"

year = int(input("Введите год: "))
print(is_leap_year(year))