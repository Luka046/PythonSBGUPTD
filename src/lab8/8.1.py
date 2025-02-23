countries = {
    "Россия": "Москва",
    "Франция": "Париж",
    "Германия": "Берлин",
    "Италия": "Рим",
    "Япония": "Токио"
}

# a) Вывод всех пар ключ-значение
print("Страны и их столицы:")
for country, capital in countries.items():
    print(f"{country}: {capital}")

# b) Вывод столицы для определенной страны
country = input("Введите страну: ")
if country in countries:
    print(f"Столица {country}: {countries[country]}")
else:
    print("Страна не найдена в словаре.")

# c) Сортировка и вывод в алфавитном порядке
print("\nСтраны в алфавитном порядке:")
for country in sorted(countries.keys()):
    print(f"{country}: {countries[country]}")